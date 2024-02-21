from Pages.BasePage import BasePage
from Config.config import ForgotPasswordData, TestData
from Pages.locators import ForgotPasswordPageLocators


class FaqPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def set_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.YOUR_EMAIL_FIELD, email)

    def click_submit_button(self):
        self.click(ForgotPasswordPageLocators.SUBMIT_BUTTON)

    def click_close_button(self):
        self.click(ForgotPasswordPageLocators.CLOSE_FORGOT_PASSWORD_BUTTON)

