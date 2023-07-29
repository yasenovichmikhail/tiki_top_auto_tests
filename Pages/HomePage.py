from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Locators"""
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")

    HEADER_LOGO = (By.XPATH, "//a[@class='HeaderLogo_link__w6i5r']")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    """Page Actions"""

    """It's used to get the page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """It's used to check sign up button"""

    def is_signup_button_exist(self):
        return self.is_visible(self.SIGNUP_BUTTON)

    def is_header_logo_exist(self):
        return self.is_visible(self.HEADER_LOGO)