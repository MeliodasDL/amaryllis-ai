# privacy_protocols.py
import hashlib
from cryptography.fernet import Fernet
from config import get_config_value  # Import the get_config_value function


class PrivacyProtocols:
    def __init__(self):
        self.encryption_key = self.load_encryption_key()
        self.cipher_suite = Fernet(self.encryption_key)

    def load_encryption_key(self):
        """
        Load the encryption key from the config.py file.
        This key will be used for encrypting and decrypting user data.
        """
        encryption_key = get_config_value("ENCRYPTION_KEY")
        return encryption_key.encode()

    def hash_password(self, password):
        """
        Hash the given password using a secure hashing algorithm (e.g., SHA-256).
         Parameters:
        password (str): The password to hash.
         Returns:
        str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def encrypt_data(self, data):
        """
        Encrypt the given data using the loaded encryption key.
         Parameters:
        data (str): The data to encrypt.
         Returns:
        bytes: The encrypted data.
        """
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the given encrypted data using the loaded encryption key.
         Parameters:
        encrypted_data (bytes): The encrypted data to decrypt.
         Returns:
        str: The decrypted data.
        """
        return self.cipher_suite.decrypt(encrypted_data).decode()


if __name__ == "__main__":
    privacy_protocols = PrivacyProtocols()
    sample_password = "my_password"
    hashed_password = privacy_protocols.hash_password(sample_password)
    print("Hashed password: ", hashed_password)
    sample_data = "This is a sample data to encrypt."
    encrypted_data = privacy_protocols.encrypt_data(sample_data)
    print("Encrypted data: ", encrypted_data)
    decrypted_data = privacy_protocols.decrypt_data(encrypted_data)
    print("Decrypted data: ", decrypted_data)