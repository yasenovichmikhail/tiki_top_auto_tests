from Pages.BasePage import BasePage
from Pages.locators import ChangePasswordLocators


class ChangePasswordPage(BasePage):

    def set_old_password(self, value):
        self.send_keys(*ChangePasswordLocators.OLD_PASSWORD_TEXT_FIELD, value)

    def set_new_password(self, value):
        self.send_keys(*ChangePasswordLocators.NEW_PASSWORD_TEXT_FIELD, value)

    def confirm_new_password(self, value):
        self.send_keys(*ChangePasswordLocators.CONFIRM_PASSWORD_TEXT_FIELD, value)

    def click_change_button(self):
        self.click(*ChangePasswordLocators.CHANGE_BUTTON)

    def click_back_button(self):
        self.click(*ChangePasswordLocators.GO_BACK_BUTTON)

