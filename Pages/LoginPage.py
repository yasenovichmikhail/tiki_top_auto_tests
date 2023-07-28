from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """Locators"""
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")

    LOGIN_TAB = (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")

    INPUT_EMAIL = (By.ID, "authorizationEmail")

    INPUT_PASSWORD = (By.ID, "authorizationPassword")

    LOGIN_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """It's used to get the page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """It's used to check sign up button"""

    def is_signup_button_exist(self):
        return self.is_visible(self.SIGNUP_BUTTON)

    """It's used to login to app"""

    def login(self, username, password):
        self.click(self.SIGNUP_BUTTON)
        self.send_keys(self.INPUT_EMAIL, username)
        self.send_keys(self.INPUT_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
