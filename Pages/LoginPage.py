import pytest
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

    def open_login_form(self):
        self.click(BasePageLocators.SIGNUP_BUTTON)

    def click_sign_up_tab(self):
        self.click(LoginPageLocators.SIGNUP_TAB)

    def click_login_tab(self):
        self.click(LoginPageLocators.LOGIN_TAB)

    def click_google_auth_button(self):
        self.click(LoginPageLocators.GOOGLE_AUTH_BUTTON)

    def click_facebook_auth_button(self):
        self.click(LoginPageLocators.FACEBOOK_AUTH_BUTTON)

    def set_email(self, email):
        self.send_keys(LoginPageLocators.INPUT_EMAIL, email)

    def set_password(self, password):
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)

    def click_forgot_password_button(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    def show_password(self):
        self.click(LoginPageLocators.SHOW_PASSWORD_ICON)

    def hide_password(self):
        self.click(LoginPageLocators.HIDE_PASSWORD_ICON)

    def click_create_my_account_button(self):
        self.click(LoginPageLocators.CREATE_MY_ACCOUNT_BUTTON)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_close_login_page(self):
        self.click(LoginPageLocators.CLOSE_LOGIN_PAGE_BUTTON)

    def login(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_login_tab()
        page.set_email(TestData.USER_EMAIL)
        page.set_password(TestData.PASSWORD)
        page.click_login_button()
