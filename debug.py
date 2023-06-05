# debug.py
import datetime

from config import get_config_value
from database import Database
from error_handling import ErrorHandling


class Debug:
    def __init__(self):
        self.error_handling = ErrorHandling()

    def log_error(self, error_message, error_code, error_resolution_suggestion):
        """
        Logs the error message, error code, and suggested resolution in a log file.
        """
        log_file = "error_log.txt"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as file:
            file.write(f"{timestamp} | Error Code: {error_code} | Error Message: {error_message}\n")
            file.write(f"Suggested Resolution: {error_resolution_suggestion}\n\n")

    def handle_error(self, error, user_email):
        """
        Handles errors by logging them and providing suggestions for resolution.
        """
        error_message, error_code, error_resolution_suggestion = self.error_handling.identify_error(error)
        self.log_error(error_message, error_code, error_resolution_suggestion)
        self.send_error_notification(user_email, error_message, error_code, error_resolution_suggestion)

    def send_error_notification(self, user_id, error_message, error_code, error_resolution_suggestion):
        """
        Sends a notification to the user with the error message, error code, and suggested resolution.
        """
        # Fetch the user's email address from the database
        db = Database()
        user_email = db.get_user_email(user_id)

        if user_email:
            print(
                f"Sending error notification to user {user_id} ({user_email}) with the following details:\nError Message: {error_message}\nError Code: {error_code}\nSuggested Resolution: {error_resolution_suggestion}")

            # Use the email configuration from config.py
            email_api_key = get_config_value("EMAIL_API_KEY")
            email_from = get_config_value("EMAIL_FROM")

            # Implement the code to send an email using the email_api_key and email_from variables.
            import sendgrid
            from sendgrid.helpers.mail import Mail, Email, To, Content

            sg = sendgrid.SendGridAPIClient(api_key=email_api_key)
            from_email = Email(email_from)
            to_email = To(user_email)
            subject = f"Amaryllis AI - Error Notification - Error Code: {error_code}"
            content = Content(
                "text/plain",
                f"Error Message: {error_message}\nError Code: {error_code}\nSuggested Resolution: {error_resolution_suggestion}"
            )
            mail = Mail(from_email, to_email, subject, content)
            response = sg.client.mail.send.post(request_body=mail.get())

        else:
            print(f"User email not found for user ID: {user_id}")

    def auto_debug(self):
        """
        Automatically debugs the application by checking for errors and providing suggestions for resolution.
        """
        try:
            # Implement code for checking errors in the application.
            raise Exception("Test error")
        except Exception as error:
            # Replace "test@example.com" with the actual user_email
            self.handle_error(error, user_email="Admin@fultonarts.com")


if __name__ == "__main__":
    debug = Debug()
    debug.auto_debug()