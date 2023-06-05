# user_data.py
import mysql.connector
from config import get_config_value

class UserData:
    def __init__(self):
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        """
        Connects to the MySQL database.
        """
        connection = mysql.connector.connect(
            host=get_config_value("DATABASE_HOST"),
            user=get_config_value("DATABASE_USER"),
            password=get_config_value("DATABASE_PASSWORD"),
            database=get_config_value("DATABASE_NAME")
        )
        return connection

    def add_user(self, user_data):
        """
        Adds a new user to the data.
        """
        cursor = self.connection.cursor()
        query = "INSERT INTO users (user_name, user_email, user_password, user_nickname, user_timezone, user_language, user_notification_preference, user_gender_preference, user_accent_preference, user_account_type, user_account_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (user_data["user_name"], user_data["user_email"], user_data["user_password"], user_data["user_nickname"], user_data["user_timezone"], user_data["user_language"], user_data["user_notification_preference"], user_data["user_gender_preference"], user_data["user_accent_preference"], user_data["user_account_type"], user_data["user_account_status"])
        cursor.execute(query, values)
        self.connection.commit()

    def update_user(self, user_id, user_data):
        """
        Updates an existing user's data.
        """
        cursor = self.connection.cursor()
        query = "UPDATE users SET "
        values = []
        for key, value in user_data.items():
            query += f"{key} = %s, "
            values.append(value)
        query = query.rstrip(", ") + " WHERE user_id = %s"
        values.append(user_id)
        cursor.execute(query, values)
        self.connection.commit()

    def get_user(self, user_id):
        """
        Retrieves user data for the given user ID.
        """
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

    def delete_user(self, user_id):
        """
        Deletes a user's data.
        """
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()

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
        "user_account_status": "active"
    }
    user_data.add_user(new_user)
    user_id = 1  # Replace with the actual user_id
    print("User added:", user_data.get_user(user_id))
    updated_data = {"user_nickname": "John"}
    user_data.update_user(user_id, updated_data)
    print("User updated:", user_data.get_user(user_id))
    user_data.delete_user(user_id)
    print("User deleted:", user_data.get_user(user_id))