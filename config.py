# config.py
import os


# Basic Configuration
APP_NAME = "Amaryllis AI"
APP_VERSION = "1.0.0"

# API Keys
API_KEY_1 = os.environ.get("API_KEY_1", "your_api_key_1")
API_KEY_2 = os.environ.get("API_KEY_2", "your_api_key_2")

# Encryption Configuration
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "your_encryption_key")

# Database Configuration
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", 3306)
DATABASE_NAME = os.environ.get("DATABASE_NAME", "AmaryllisAI")
DATABASE_USER = os.environ.get("DATABASE_USER", "root")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "@$_wvHDyZAm_")

# Email Configuration
EMAIL_API_KEY = os.environ.get("EMAIL_API_KEY", ";Ab0(p+}xP)9")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "AI@Amaryllis.com")

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "your_twilio_phone_number")

# Stripe Configuration
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "your_stripe_api_key")

# PayPal Configuration
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID", "your_paypal_client_id")
PAYPAL_CLIENT_SECRET = os.environ.get("PAYPAL_CLIENT_SECRET", "your_paypal_client_secret")

# Other Configuration
# Add any other configuration settings here as needed.
UPDATE_URL = "https://example.com/update"
IMAGE_MODEL_PATH = os.environ.get("IMAGE_MODEL_PATH", "path/to/image/generation/model")
IP_GEOLOCATION_API_KEY = os.environ.get("IP_GEOLOCATION_API_KEY", "your_ip_geolocation_api_key")

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
