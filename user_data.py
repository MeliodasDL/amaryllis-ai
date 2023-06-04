# user_data.py
import os
import json


class UserData:
    def __init__(self, data_file="user_data.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads user data from the data file or creates a new file if it doesn't exist.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = {}
            with open(self.data_file, "w") as file:
                json.dump(data, file)
        return data

    def save_data(self):
        """
        Saves the current user data to the data file.
        """
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)

    def add_user(self, user_id, user_data):
        """
        Adds a new user to the data.
        """
        self.data[user_id] = user_data
        self.save_data()

    def update_user(self, user_id, user_data):
        """
        Updates an existing user's data.
        """
        if user_id in self.data:
            self.data[user_id].update(user_data)
            self.save_data()

    def get_user(self, user_id):
        """
        Retrieves user data for the given user ID.
        """
        return self.data.get(user_id, None)

    def delete_user(self, user_id):
        """
        Deletes a user's data.
        """
        if user_id in self.data:
            del self.data[user_id]
            self.save_data()


if __name__ == "__main__":
    user_data = UserData()
    # Example usage
    new_user = {
        "user_name": "John Doe",
        "user_email": "john.doe@example.com",
        "user_password": "password123",
        "user_nickname": "Johnny",
        "user_timezone": "UTC",
        "user_language": "en",
        "user_notification_preference": "email",
        "user_gender_preference": "male",
        "user_accent_preference": "British",
        "user_account_type": "free",
        "user_account_status": "active",
        "user_experience_data": {},
        "user_feedback": [],
        "user_bug_report": []
    }
    user_id = "user_001"
    user_data.add_user(user_id, new_user)
    print("User added:", user_data.get_user(user_id))
    updated_data = {"user_nickname": "John"}
    user_data.update_user(user_id, updated_data)
    print("User updated:", user_data.get_user(user_id))
    user_data.delete_user(user_id)
    print("User deleted:", user_data.get_user(user_id))
