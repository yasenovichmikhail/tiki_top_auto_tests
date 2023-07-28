import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_signup_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_button_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)

