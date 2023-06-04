import os
import shutil
import time
import datetime
import logging


class Backup:
    def __init__(self, backup_directory="backups"):
        self.backup_directory = backup_directory
        self.timestamp_format = "%Y%m%d_%H%M%S"
        self.setup_backup_directory()

    def setup_backup_directory(self):
        """
        Create the backup directory if it does not exist.
        """
        if not os.path.exists(self.backup_directory):
            os.makedirs(self.backup_directory)
            logging.info(f"Backup directory '{self.backup_directory}' created.")

    def create_backup(self, source_directory, backup_name=None):
        """
        Create a backup of the given source_directory.
         :param source_directory: The directory to be backed up.
        :param backup_name: Optional custom name for the backup folder. Defaults to None.
        :return: The path of the created backup folder.
        """
        if not os.path.exists(source_directory):
            logging.error(f"Source directory '{source_directory}' not found. Backup not created.")
            return None

        timestamp = datetime.datetime.now().strftime(self.timestamp_format)
        backup_name = backup_name or f"{source_directory}_{timestamp}"
        backup_path = os.path.join(self.backup_directory, backup_name)

        try:
            shutil.copytree(source_directory, backup_path)
            logging.info(f"Backup created: '{backup_path}'")
            return backup_path
        except Exception as e:
            logging.error(f"Error creating backup: {e}")
            return None

    def clean_old_backups(self, max_backups=5):
        """
        Remove old backups, keeping only the latest 'max_backups' backups.
         :param max_backups: Maximum number of backups to keep. Defaults to 5.
        """
        backups = [os.path.join(self.backup_directory, d) for d in os.listdir(self.backup_directory)]
        backups = sorted(backups, key=os.path.getctime, reverse=True)

        if len(backups) > max_backups:
            for backup in backups[max_backups:]:
                try:
                    shutil.rmtree(backup)
                    logging.info(f"Removed old backup: '{backup}'")
                except Exception as e:
                    logging.error(f"Error removing old backup '{backup}': {e}")


if __name__ == "__main__":
    backup_manager = Backup()
    # Example usage:
    source_directory = "data"
    backup_manager.create_backup(source_directory)
    backup_manager.clean_old_backups(max_backups=5)
