from chatbot import Chatbot
from database import Database
from user_interface import UserInterface
from backup import Backup
from debug import Debug
from security import Security
from encryption import Encryption
from user_data import UserData
from error_handling import ErrorHandling
from update import Update
from feedback import Feedback
from troubleshooting import Troubleshooting
from account_settings import AccountSettings
from premium_features import PremiumFeatures
from image_generation import ImageGeneration
from video_generation import VideoGeneration
from natural_language_processing import NaturalLanguageProcessing
from communication_preferences import CommunicationPreferences
from legal_restrictions import LegalRestrictions
from privacy_protocols import PrivacyProtocols
from user_experience_data import UserExperienceData
from config import get_config_value


def run_application():
    # Initialize classes with necessary configuration values
    database = Database(
        host=get_config_value("DATABASE_HOST"),
        port=get_config_value("DATABASE_PORT"),
        user=get_config_value("DATABASE_USER"),
        password=get_config_value("DATABASE_PASSWORD"),
        database_name=get_config_value("DATABASE_NAME")
    )
    user_interface = UserInterface()
    chatbot = Chatbot(
    api_key_1=get_config_value("API_KEY_1"),
    api_key_2=get_config_value("API_KEY_2"),
    email_api_key=get_config_value("EMAIL_API_KEY"),
    email_from=get_config_value("EMAIL_FROM"),
    twilio_account_sid=get_config_value("TWILIO_ACCOUNT_SID"),
    twilio_auth_token=get_config_value("TWILIO_AUTH_TOKEN"),
    twilio_phone_number=get_config_value("TWILIO_PHONE_NUMBER")
    )
    backup = Backup()
    debug = Debug()
    security = Security()
    encryption = Encryption()
    user_data = UserData(database=database)
    error_handling = ErrorHandling()
    update = Update()
    feedback = Feedback()
    troubleshooting = Troubleshooting()
    account_settings = AccountSettings()
    premium_features = PremiumFeatures()
    image_generation = ImageGeneration()
    video_generation = VideoGeneration()
    natural_language_processing = NaturalLanguageProcessing()
    communication_preferences = CommunicationPreferences()
    legal_restrictions = LegalRestrictions()
    privacy_protocols = PrivacyProtocols()
    user_experience_data = UserExperienceData()

    # Main application loop
    while user_interface.is_application_running():
        # Display login/registration screen
        user_interface.create_login_screen()
        # Check user login/registration input and proceed to home screen if successful
        if user_interface.validate_login_registration():
            user_interface.create_home_screen()
            # Main chatbot interaction loop
            while user_interface.is_user_logged_in():
                # Get user input and process it with the chatbot
                user_input = user_interface.get_user_input()
                chatbot_response = chatbot.process_input(user_input)
                # Display chatbot response on the user interface
                user_interface.display_chatbot_response(chatbot_response)
                # Update user experience data based on the interaction
                user_experience_data.update(chatbot_response)
        else:
            # If login/registration unsuccessful, display an error message and return to the login/registration screen
            user_interface.display_error_message("Invalid login or registration information. Please try again.")


if __name__ == "__main__":
    run_application()