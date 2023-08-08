import pytest

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):
    def test_signup_button_is_visible(self):
        page = BasePage(self.driver)
        page.is_signup_button_exist()

    def test_home_page_title(self):
        page = HomePage(self.driver)
        page.check_home_page_title()

    def test_guest_can_see_header_logo(self):
        page = BasePage(self.driver)
        page.is_header_logo_visible()

    def test_guest_can_see_header(self):
        page = BasePage(self.driver)
        page.is_header_visible()

    def test_guest_can_see_boost_your_profile_section(self):
        page = HomePage(self.driver)
        page.is_boost_your_profile_container_presented()

    def test_guest_can_see_footer(self):
        page = BasePage(self.driver)
        page.is_footer_visible()

