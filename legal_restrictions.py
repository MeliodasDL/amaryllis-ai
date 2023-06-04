# legal_restrictions.py
import re
import json


class LegalRestrictions:
    def __init__(self):
        self.restricted_actions = self.load_restricted_actions()

    def load_restricted_actions(self):
        """
        Load restricted actions from a JSON file or other data source.
        This file should contain a list of actions that the chatbot is not allowed to perform.
        """
        with open('restricted_actions.json', 'r') as file:
            restricted_actions = json.load(file)
        return restricted_actions

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
