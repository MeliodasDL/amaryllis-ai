import sqlite3
import os


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        if not os.path.exists(self.db_name):
            self.create_database()
        self.connection = sqlite3.connect(self.db_name)

    def close(self):
        if self.connection:
            self.connection.close()

    def create_database(self):
        self.connect()
        self.create_user_table()
        self.create_other_tables()
        self.close()

    def create_user_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                user_email TEXT UNIQUE NOT NULL,
                user_password TEXT NOT NULL,
                user_nickname TEXT,
                user_timezone TEXT,
                user_language TEXT,
                user_notification_preference TEXT,
                user_gender_preference TEXT,
                user_accent_preference TEXT,
                user_account_type TEXT,
                user_account_status TEXT
            )
        """)
        self.connection.commit()

    def create_other_tables(self):
        # Add code to create other necessary tables here
        pass

    def insert_user(self, user_data):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (
                user_name, user_email, user_password, user_nickname,
                user_timezone, user_language, user_notification_preference,
                user_gender_preference, user_accent_preference, user_account_type,
                user_account_status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, user_data)
        self.connection.commit()

    def update_user(self, user_id, user_data):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users SET
                user_name = ?, user_email = ?, user_password = ?, user_nickname = ?,
                user_timezone = ?, user_language = ?, user_notification_preference = ?,
                user_gender_preference = ?, user_accent_preference = ?, user_account_type = ?,
                user_account_status = ?
            WHERE user_id = ?
        """, user_data + (user_id,))
        self.connection.commit()

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        self.connection.commit()

    def get_user_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone()

    def get_user_by_email(self, user_email):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_email = ?", (user_email,))
        return cursor.fetchone()

    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()


if __name__ == "__main__":
    db = Database("AmaryllisAI.db")
    db.connect()
    # Add code to test database functionality here
    db.close()
