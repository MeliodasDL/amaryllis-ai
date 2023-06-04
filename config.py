# config.py
import os


# Basic Configuration
APP_NAME = "Amaryllis AI"
APP_VERSION = "1.0.0"

# API Keys
API_KEY_1 = os.environ.get("API_KEY_1", "your_api_key_1")
API_KEY_2 = os.environ.get("API_KEY_2", "your_api_key_2")

# Database Configuration
DATABASE_HOST = os.environ.get("DATABASE_HOST", "your_database_host")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "your_database_port")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "your_database_name")
DATABASE_USER = os.environ.get("DATABASE_USER", "your_database_user")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "your_database_password")

# Email Configuration
EMAIL_API_KEY = os.environ.get("EMAIL_API_KEY", "your_email_api_key")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "your_email_from_address")

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "your_twilio_phone_number")

# Other Configuration
# Add any other configuration settings here as needed.


def get_config_value(key, default=None):
    """
    Get the value of a configuration setting by its key.
     Parameters:
    key (str): The key of the configuration setting.
    default: The default value to return if the key is not found.
     Returns:
    The value of the configuration setting or the default value if the key is not found.
    """
    return globals().get(key, default)
