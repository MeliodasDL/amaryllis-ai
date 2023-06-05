# security.py
import hashlib
import os
import json
from encryption import Encryption
import config  # Import the config module


class Security:
    def __init__(self):
        self.encryption = Encryption(config.ENCRYPTION_KEY)  # Use the encryption key from config

    def hash_password(self, password):
        """
        Hashes the given password using a secure hashing algorithm.
        """
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt, key

    def verify_password(self, password, salt, key):
        """
        Verifies if the given password matches the stored salt and key.
        """
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return new_key == key

    def secure_user_data(self, user_data):
        """
        Secures user data by encrypting sensitive information.
        """
        return self.encryption.encrypt(json.dumps(user_data))

    def retrieve_user_data(self, encrypted_data):
        """
        Retrieves user data by decrypting the encrypted data.
        """
        return json.loads(self.encryption.decrypt(encrypted_data))

    def secure_api_key(self, api_key):
        """
        Secures the API key by encrypting it.
        """
        return self.encryption.encrypt(api_key)

    def retrieve_api_key(self, encrypted_api_key):
        """
        Retrieves the API key by decrypting the encrypted API key.
        """
        return self.encryption.decrypt(encrypted_api_key)


if __name__ == "__main__":
    security = Security()
    # Example usage
    password = "my_password"
    salt, key = security.hash_password(password)
    print(security.verify_password(password, salt, key))
    user_data = {"username": "user1", "email": "user1@example.com"}
    encrypted_data = security.secure_user_data(user_data)
    print(security.retrieve_user_data(encrypted_data))
    api_key = "my_api_key"
    encrypted_api_key = security.secure_api_key(api_key)
    print(security.retrieve_api_key(encrypted_api_key))
