# legal_restrictions.py
import re
import json
import requests
from database import Database
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD
from config import IP_GEOLOCATION_API_KEY


class LegalRestrictions:
    def __init__(self):
        self.db = Database(DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD)
        self.restricted_actions = self.load_restricted_actions()

    def load_restricted_actions(self):
        """
        Load restricted actions from the restricted_actions table.
        """
        restricted_actions = self.db.fetch_all("SELECT action FROM restricted_actions")
        return [action[0] for action in restricted_actions]

    def get_local_laws(self, user_ip):
        """
        Fetch local laws based on the user's IP address.
        """
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={IP_GEOLOCATION_API_KEY}&ip={user_ip}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            country = data.get("country_name", "")
            # Fetch local laws based on the country
            local_laws = self.db.fetch_all("SELECT restricted_action FROM local_laws WHERE country = %s", (country,))
            # Insert local laws into the restricted_actions table
            for law in local_laws:
                self.db.execute("INSERT INTO restricted_actions (action) VALUES (%s)", (law[0],))
            # Reload restricted actions
            self.restricted_actions = self.load_restricted_actions()
        else:
            print("Error fetching IP Geolocation data")

    def is_action_legal(self, action):
        """
        Check if the given action is legal or not.
         Parameters:
        action (str): The action to check.
         Returns:
        bool: True if the action is legal, False otherwise.
        """
        return not any(
            re.search(restricted_action, action, re.IGNORECASE)
            for restricted_action in self.restricted_actions
        )

    def filter_illegal_content(self, content):
        """
        Filter out any illegal content from the given content.
         Parameters:
        content (str): The content to filter.
         Returns:
        str: The filtered content.
        """
        for restricted_action in self.restricted_actions:
            content = re.sub(restricted_action, '[REDACTED]', content, flags=re.IGNORECASE)
        return content

    def enforce_legal_restrictions(self, chatbot_response):
        """
        Enforce legal restrictions on the chatbot's response.
         Parameters:
        chatbot_response (str): The chatbot's response.
         Returns:
        str: The chatbot's response with legal restrictions enforced.
        """
        if not self.is_action_legal(chatbot_response):
            chatbot_response = self.filter_illegal_content(chatbot_response)
        return chatbot_response


if __name__ == "__main__":
    legal_restrictions = LegalRestrictions()
    sample_action = "I will hack into the user's account."
    print("Is action legal? ", legal_restrictions.is_action_legal(sample_action))
    sample_content = "I can help you with hacking into someone's account."
    print("Filtered content: ", legal_restrictions.filter_illegal_content(sample_content))
    sample_response = "Sure, I can help you with hacking into their account."
    print("Enforced legal restrictions: ", legal_restrictions.enforce_legal_restrictions(sample_response))
