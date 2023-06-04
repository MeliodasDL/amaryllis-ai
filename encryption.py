# encryption.py
from cryptography.fernet import Fernet
import base64
import os
from config import get_config_value

class Encryption:
    def __init__(self):
        self.key = get_config_value("ENCRYPTION_KEY")
        self.fernet = Fernet(self.key)

    def encrypt(self, data):
        """
        Encrypts the given data using the Fernet encryption.
        """
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data):
        """
        Decrypts the encrypted data using the Fernet encryption.
        """
        return self.fernet.decrypt(encrypted_data.encode()).decode()


if __name__ == "__main__":
    encryption = Encryption()
    # Example usage
    data = "This is a test message."
    encrypted_data = encryption.encrypt(data)
    print("Encrypted data:", encrypted_data)

    decrypted_data = encryption.decrypt(encrypted_data)
    print("Decrypted data:", decrypted_data)
