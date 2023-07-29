import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):

    def test_signup_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_signup_button_exist(), "Sign Up button is not presented"

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE), "Title doesn't match"

    def test_header_logo_visible(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.is_header_logo_exist(), "Header logo is not presented"
