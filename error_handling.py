# feedback.py
import os
import sys
import json
import datetime
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class ErrorHandling:
    # No implementation needed for now
    pass


class Feedback:
    def __init__(self, user_id, feedback_type, feedback_content, timestamp=None):
        self.user_id = user_id
        self.feedback_type = feedback_type
        self.feedback_content = feedback_content
        self.timestamp = timestamp or datetime.datetime.now()

    def save_feedback(self, database):
        """
        Save the feedback to the database.
        :param database: The database object to save the feedback to.
        """
        feedback_data = {
            'user_id': self.user_id,
            'feedback_type': self.feedback_type,
            'feedback_content': self.feedback_content,
            'timestamp': self.timestamp
        }
        database.save_feedback(feedback_data)

    def send_feedback_email(self, email_settings):
        """
        Send the feedback content as an email to the specified email address.
        :param email_settings: A dictionary containing the email settings, such as the recipient email address, subject, etc.
        """
        # Set up the email content and settings
        message = Mail(
            from_email=email_settings['from_email'],
            to_emails=email_settings['to_email'],
            subject=email_settings['subject'],
            html_content=self.feedback_content
        )
        # Send the email using the SendGrid API
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)


def collect_feedback(user_id):
    """
    Collect feedback from the user.
    :param user_id: The ID of the user providing the feedback.
    :return: A Feedback object containing the collected feedback.
    """
    print("Please select a feedback type:")
    print("1. Bug report")
    print("2. Feature request")
    print("3. General feedback")
    feedback_type = int(input("Enter the number corresponding to the feedback type: "))
    feedback_content = input("Please enter your feedback: ")
    return Feedback(user_id, feedback_type, feedback_content)


def main(database, email_settings):
    """
    The main function for the feedback module.
    :param database: The database object to save the feedback to.
    :param email_settings: A dictionary containing the email settings, such as the recipient email address, subject, etc.
    """
    user_id = input("Enter your user ID: ")
    feedback = collect_feedback(user_id)
    feedback.save_feedback(database)
    feedback.send_feedback_email(email_settings)
    print("Thank you for your feedback!")


if __name__ == "__main__":
    # Replace with your actual database object and email settings
    class Database:
        def save_feedback(self, feedback_data):
            """
            Save the feedback data to the database.
            :param feedback_data: A dictionary containing the feedback data to be saved.
            """
            # TODO: Implement the function to save the feedback data to the database
            # Placeholder implementation
            with open('feedback_data.json', 'a') as f:
                json.dump(feedback_data, f)
                f.write('\n')


    database = Database()
    email_settings = {
        'from_email': 'noreply@example.com',
        'to_email': 'feedback@example.com',
        'subject': 'Amaryllis AI Feedback'
    }
    main(database, email_settings)
