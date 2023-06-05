import mysql.connector
import config

class UserExperienceData:
    def __init__(self):
        self.db_connection = self.connect_to_database()

    def connect_to_database(self):
        """
        Connect to the MySQL database using the configuration settings from config.py.
        """
        connection = mysql.connector.connect(
            host=config.DATABASE_HOST,
            user=config.DATABASE_USER,
            password=config.DATABASE_PASSWORD,
            database=config.DATABASE_NAME
        )
        return connection

    def store_user_experience(self, user_id, experience_data):
        """
        Store user experience data for a specific user.
         Parameters:
        user_id (str): The unique identifier for the user.
        experience_data (dict): The experience data to store for the user.
        """
        cursor = self.db_connection.cursor()
        query = "INSERT INTO user_experience_data (user_id, interaction, content, response_time, sentiment) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, experience_data["interaction"], experience_data["content"], experience_data["response_time"], experience_data["sentiment"])
        cursor.execute(query, values)
        self.db_connection.commit()

    def get_user_experience(self, user_id):
        """
        Retrieve user experience data for a specific user.
         Parameters:
        user_id (str): The unique identifier for the user.
         Returns:
        list: A list of experience data for the specified user.
        """
        cursor = self.db_connection.cursor()
        query = "SELECT interaction, content, response_time, sentiment FROM user_experience_data WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        experience_data = [{"interaction": row[0], "content": row[1], "response_time": row[2], "sentiment": row[3]} for row in result]
        return experience_data

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