# update.py
import datetime
import os
import shutil

import requests

import config


class Update:
    def __init__(self, current_version):
        self.current_version = current_version
        self.update_url = config.get_config_value("UPDATE_URL")

    def check_for_updates(self):
        """
        Check for updates by comparing the current version with the latest version available on the server.
        """
        try:
            response = requests.get(self.update_url)
            response.raise_for_status()
            latest_version = response.json()["latest_version"]
            if self.current_version < latest_version:
                return True, latest_version
            else:
                return False, None
        except requests.exceptions.RequestException as e:
            print(f"Error checking for updates: {e}")
            return False, None
        except ValueError:
            print("Error parsing the update server response.")
            return False, None

    def download_update(self, latest_version):
        """
        Download the update files from the server.
        """
        try:
            update_files_url = f"{self.update_url}/{latest_version}/files"
            response = requests.get(update_files_url)
            if response.status_code == 200:
                update_files = response.json()["files"]
                for file in update_files:
                    file_url = f"{update_files_url}/{file}"
                    file_response = requests.get(file_url)
                    with open(file, "wb") as f:
                        f.write(file_response.content)
                return True
            else:
                print(f"Error downloading update files: {response.status_code}")
                return False
        except Exception as e:
            print(f"Error downloading update files: {e}")
            return False

    def install_update(self, latest_version):
        """
        Install the update by replacing the current application files with the downloaded update files.
        """
        try:
            # Backup current application files
            backup_folder = f"backup_{self.current_version}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            os.makedirs(backup_folder)
            for file in os.listdir():
                if file.endswith(".py"):
                    os.rename(file, f"{backup_folder}/{file}")
            # Move downloaded update files to the main application folder
            for file in os.listdir("update_files"):
                os.rename(f"update_files/{file}", file)
            # Update the current_version variable
            self.current_version = latest_version
            return True
        except Exception as e:
            print(f"Error installing update: {e}")
            return False

    def perform_update(self):
        """
        Check for updates, download and install them if available.
        """
        updates_available, latest_version = self.check_for_updates()
        if updates_available:
            print(f"Update available: {latest_version}")
            print("Downloading update...")
            if self.download_update(latest_version):
                print("Update downloaded successfully.")
                print("Installing update...")
                if self.install_update(latest_version):
                    print("Update installed successfully.")
                    return True
                else:
                    print("Error installing update.")
                    return False
            else:
                print("Error downloading update.")
                return False
        else:
            print("No updates available.")
            return False

    def clean_up(self, backup_folder, update_files_folder):
        """
        Remove the backup folder and update files folder after a successful or failed update.
        """
        try:
            shutil.rmtree(backup_folder)
            shutil.rmtree(update_files_folder)
        except Exception as e:
            print(f"Error cleaning up after update: {e}")


if __name__ == "__main__":
    current_version = config.get_config_value("APP_VERSION")
    updater = Update(current_version)
    if updater.perform_update():
        print("Update process completed successfully.")
    else:
        print("Update process failed.")
