# user_experience_data.py
import json
import os


class UserExperienceData:
    def __init__(self, data_file="user_experience_data.json"):
        self.data_file = data_file
        self.user_experience_data = self.load_user_experience_data()

    def load_user_experience_data(self):
        """
        Load user experience data from a JSON file or other data source.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as file:
                json.dump({}, file)

        with open(self.data_file, "r") as file:
            user_experience_data = json.load(file)
        return user_experience_data

    def save_user_experience_data(self):
        """
        Save user experience data to a JSON file or other data source.
        """
        with open(self.data_file, "w") as file:
            json.dump(self.user_experience_data, file)

    def store_user_experience(self, user_id, experience_data):
        """
        Store user experience data for a specific user.
         Parameters:
        user_id (str): The unique identifier for the user.
        experience_data (dict): The experience data to store for the user.
        """
        if user_id not in self.user_experience_data:
            self.user_experience_data[user_id] = []
        self.user_experience_data[user_id].append(experience_data)
        self.save_user_experience_data()

    def get_user_experience(self, user_id):
        """
        Retrieve user experience data for a specific user.
         Parameters:
        user_id (str): The unique identifier for the user.
         Returns:
        list: A list of experience data for the specified user.
        """
        return self.user_experience_data.get(user_id, [])


if __name__ == "__main__":
    user_experience_data = UserExperienceData()
    sample_user_id = "user123"
    sample_experience_data = {
        "interaction": "text",
        "content": "Sample text message",
        "response_time": 1.5,
        "sentiment": "positive",
    }
    user_experience_data.store_user_experience(sample_user_id, sample_experience_data)
    retrieved_experience_data = user_experience_data.get_user_experience(sample_user_id)
    print(
        f"Retrieved experience data for user {sample_user_id}: {retrieved_experience_data}"
    )
