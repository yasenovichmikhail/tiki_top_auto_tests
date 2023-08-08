import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_signup_button_visible(self):
        page = LoginPage(self.driver)
        page.is_signup_button_exist()

    def test_login(self):
        page = LoginPage(self.driver)
        page.login(TestData.USER_NAME, TestData.PASSWORD)

