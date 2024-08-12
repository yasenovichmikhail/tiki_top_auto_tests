import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, LoginPageLocators, ForgotPasswordPageLocators, HomePageLocators


class LoginPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """It's used to login to app"""

    def open_login_form(self):
        self.click(BasePageLocators.SIGNUP_BUTTON)
        actual_login_tab_text = self.get_element_text(LoginPageLocators.LOGIN_TAB)
        expected_login_tab_text = "Log in"
        assert actual_login_tab_text == expected_login_tab_text, f"Expected {expected_login_tab_text}, " \
                                                                 f"got {actual_login_tab_text}"

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

    def is_required_field(self):
        # self.click(LoginPageLocators.CREATE_MY_ACCOUNT_BUTTON)
        actual_warning = self.get_element_text(LoginPageLocators.REQUIRED_FIELD_WARNING)
        expected_warning = 'Required'
        assert actual_warning == expected_warning, f"Expected {expected_warning}, got {actual_warning}"

    def set_password(self, password):
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)

    def click_forgot_password_button(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        actual_header = self.get_element_text(ForgotPasswordPageLocators.FORGOT_PASSWORD_FORM_HEADER)
        expected_header = "ENTER YOUR EMAIL"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def show_password(self):
        self.click(LoginPageLocators.SHOW_PASSWORD_ICON)

    def hide_password(self):
        self.click(LoginPageLocators.HIDE_PASSWORD_ICON)

    def click_create_my_account_button(self):
        self.click(LoginPageLocators.CREATE_MY_ACCOUNT_BUTTON)

    def click_create_account_disabled_button(self):
        self.click(LoginPageLocators.CREATE_ACCOUNT_DISABLED_BUTTON)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_close_login_page(self):
        self.click(LoginPageLocators.CLOSE_LOGIN_PAGE_BUTTON)
        self.is_not_element_present(LoginPageLocators.LOGIN_TAB, 4)

    def login(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_login_tab()
        page.set_email(TestData.USER_EMAIL)
        page.set_password(TestData.PASSWORD)
        page.click_login_button()
