import pytest

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.ContuctUsPage import ContactUsPage
from Tests.test_base import BaseTest


class TestContactUs(BaseTest):
    def test_signup_button_is_visible(self):
        page = ContactUsPage(self.driver)
        page.is_signup_button_exist()

    def test_contact_us_page_title(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.check_contact_us_page_title()

    def test_guest_can_see_header_logo_from_contact_us_page(self):
        page = ContactUsPage(self.driver)
        page.is_header_logo_visible()

    def test_guest_can_see_header_from_contact_us_page(self):
        page = ContactUsPage(self.driver)
        page.is_header_visible()

    def test_guest_can_see_footer_from_contact_us_page(self):
        page = ContactUsPage(self.driver)
        page.is_footer_visible()

    def test_guest_can_see_get_free_views_from_contact_us_page(self):
        page = ContactUsPage(self.driver)
        page.is_get_free_views_visible()

    def test_guest_can_see_get_in_touch_container_form(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_contact_us_container_form_presented()

    def test_guest_can_see_first_name_text_field(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_first_name_text_field_presented()

    def test_guest_can_see_first_name_text_field_placeholder(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_first_name_text_field_placeholder_presented()


