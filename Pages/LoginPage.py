from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """It's used to login to app"""

    def login(self, username, password):
        self.click(BasePageLocators.SIGNUP_BUTTON)
        self.send_keys(LoginPageLocators.INPUT_EMAIL, username)
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
