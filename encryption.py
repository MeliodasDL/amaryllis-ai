# encryption.py
from cryptography.fernet import Fernet
import base64
import os


class Encryption:
    def __init__(self):
        self.key = self.load_key()
        self.fernet = Fernet(self.key)

    def load_key(self):
        """
        Loads the encryption key from a file or generates a new one if it doesn't exist.
        """
        key_file = "encryption_key.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as file:
                key = file.read()
        else:
            key = base64.urlsafe_b64encode(os.urandom(32))
            with open(key_file, "wb") as file:
                file.write(key)
        return key

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
