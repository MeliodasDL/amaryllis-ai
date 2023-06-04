import mysql.connector
from mysql.connector import Error

# Import required variables from config.py
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

class Database:
    def __init__(self, db_name=DATABASE_NAME):
        self.db_name = db_name
        self.connection = None
        self.connect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=DATABASE_HOST,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                database=self.db_name  # Use self.db_name attribute
            )
            if not self.connection.is_connected():
                self.create_database()
        except Error as e:
            print(f"Error: {e}")

    # Other methods remain the same

if __name__ == "__main__":
    with Database() as db:
        # Example usage:
        db.insert_user("JohnDoe", "john.doe@example.com", "secure_password")
        with db.connection.cursor() as cursor:  # Use context manager for the cursor
            cursor.execute("SELECT * FROM users WHERE user_email = %s", ("john.doe@example.com",))
            user = cursor.fetchone()
            print(user)

        db.update_user_setting(user[0], "user_nickname", "Johnny")
        with db.connection.cursor() as cursor:  # Use context manager for the cursor
            cursor.execute("SELECT * FROM users WHERE user_email = %s", ("john.doe@example.com",))
            updated_user = cursor.fetchone()
            print(updated_user)

    def close(self):
        if self.connection:
            self.connection.close()

    def create_database(self):
        self.create_user_table()
        self.create_other_tables()

    def create_user_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_name VARCHAR(255) NOT NULL,
                user_email VARCHAR(255) UNIQUE NOT NULL,
                user_password VARCHAR(255) NOT NULL,
                user_nickname VARCHAR(255),
                user_timezone VARCHAR(255),
                user_language VARCHAR(255),
                user_notification_preference VARCHAR(255),
                user_gender_preference VARCHAR(255),
                user_accent_preference VARCHAR(255),
                user_account_type VARCHAR(255),
                user_account_status VARCHAR(255)
            )
        """)
        self.connection.commit()

    def create_other_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS premium_features (
                feature_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                feature_name VARCHAR(255) NOT NULL,
                feature_description TEXT NOT NULL,
                feature_price FLOAT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_settings (
                setting_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                setting_name VARCHAR(255) UNIQUE NOT NULL,
                setting_value TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS restricted_actions (
                action_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                action_name VARCHAR(255) UNIQUE NOT NULL,
                action_description TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS error_messages (
                error_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                error_code INTEGER UNIQUE NOT NULL,
                error_message TEXT NOT NULL,
                error_resolution_suggestion TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_experience_data (
                data_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER NOT NULL,
                experience_data TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        cursor.execute("""
           CREATE TABLE IF NOT EXISTS feedback_data (
                feedback_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER NOT NULL,
                feedback_type VARCHAR(255) NOT NULL,
                feedback_content TEXT NOT NULL,
                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        self.connection.commit()

    def insert_user(self, user_name, user_email, user_password):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (user_name, user_email, user_password)
            VALUES (%s, %s, %s)
        """, (user_name, user_email, user_password))
        self.connection.commit()

    def get_user_by_email(self, user_email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM users
            WHERE user_email = %s
        """, (user_email,))
        return cursor.fetchone()

    def update_user_setting(self, user_id, setting_name, setting_value):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users
            SET {} = %s
            WHERE user_id = %s
        """.format(setting_name), (setting_value, user_id))
        self.connection.commit()

    # Add more methods for interacting with the database as needed.

if __name__ == "__main__":
    with Database() as db:
        # Example usage:
        db.insert_user("JohnDoe", "john.doe@example.com", "secure_password")
        user = db.get_user_by_email("john.doe@example.com")
        print(user)

        db.update_user_setting(user[0], "user_nickname", "Johnny")
        updated_user = db.get_user_by_email("john.doe@example.com")
        print(updated_user)
