import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_login_tab()
        page.set_email(TestData.USER_EMAIL)
        page.set_password(TestData.PASSWORD)
        page.click_login_button()

    def test_user_can_open_login_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()

    def test_user_can_close_logit_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_close_login_page()

    def test_user_can_open_forgot_password_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_forgot_password_button()

