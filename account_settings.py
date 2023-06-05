# Import necessary libraries and modules
import hashlib

from database import Database


class AccountSettings:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()
        self.user_data = self.db.get_user_data(user_id)

    def change_password(self, old_password, new_password):
        """
        Change the user's password.
         :param old_password: The user's current password.
        :param new_password: The new password the user wants to set.
        :return: A message indicating the success or failure of the operation.
        """
        # Verify the old password
        if hashlib.sha256(old_password.encode()).hexdigest() == self.user_data['user_password']:
            # Update the password in the database
            self.db.update_user_password(self.user_id, hashlib.sha256(new_password.encode()).hexdigest())
            return "Password changed successfully."
        else:
            return "Incorrect old password. Please try again."

    def update_account_settings(self, settings):
        """
        Update the user's account settings.
         :param settings: A dictionary containing the updated settings.
        :return: A message indicating the success or failure of the operation.
        """
        # Update the user's settings in the database
        self.db.update_user_settings(self.user_id, settings)
        return "Account settings updated successfully."

    def upgrade_account(self, account_type):
        """
        Upgrade the user's account to a premium tier.
         :param account_type: The premium account type the user wants to upgrade to.
        :return: A message indicating the success or failure of the operation.
        """
        # Verify the user's current account type
        if self.user_data['user_account_type'] == 'free':
            # Update the user's account type in the database
            self.db.update_user_account_type(self.user_id, account_type)
            return f"Account upgraded to {account_type} successfully."
        else:
            return "Your account is already a premium account."

    def disable_account(self):
        """
        Disable the user's account.
         :return: A message indicating the success or failure of the operation.
        """
        if self.user_data['user_account_status'] != 'active':
            return "Your account is already disabled."
        # Update the user's account status in the database
        self.db.update_user_account_status(self.user_id, 'disabled')
        return "Account disabled successfully."

    def enable_account(self):
        """
        Enable the user's account.
         :return: A message indicating the success or failure of the operation.
        """
        if self.user_data['user_account_status'] != 'disabled':
            return "Your account is already active."
        # Update the user's account status in the database
        self.db.update_user_account_status(self.user_id, 'active')
        return "Account enabled successfully."


if __name__ == "__main__":
    # Example usage
    account_settings = AccountSettings(user_id=1)
    print(account_settings.change_password("old_password", "new_password"))
    print(account_settings.update_account_settings({"user_timezone": "UTC", "user_language": "en"}))
    print(account_settings.upgrade_account("premium"))
    print(account_settings.disable_account())
    print(account_settings.enable_account())
