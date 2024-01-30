import time

import pytest

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.ContuctUsPage import ContactUsPage
from Tests.test_base import BaseTest


class TestContactUsGeneral(BaseTest):

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

    def test_guest_can_go_to_home_page_from_header_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.go_to_home_page_from_header_link()

    def test_guest_can_go_to_pricing_page_from_header_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.go_to_pricing_page_from_header_link()

    def test_guest_can_go_to_faq_page_from_header_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.go_to_faq_page_from_header_link()

    def test_guest_can_go_to_learn_page_from_header_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.go_to_learn_page_from_header_link()

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

    def test_guest_can_see_email_address_text_field(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_email_address_text_field_presented()

    def test_guest_can_see_email_address_text_field_placeholder(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_email_address_text_field_placeholder_presented()

    def test_guest_can_see_message_text_area(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_message_text_area_presented()

    def test_guest_can_see_message_text_area_placeholder(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_message_text_area_placeholder_presented()

    def test_guest_can_see_send_message_button(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_send_message_button_presented()

    def test_guest_can_see_privacy_policy_button(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_privacy_policy_button_presented()

    def test_guest_can_open_privacy_policy_from_contact_us_page(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_privacy_policy_opened()

    def test_guest_can_go_to_home_page_from_footer_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_footer_link()
        page.go_to_home_page_from_footer_link()

    def test_guest_can_go_to_pricing_page_from_footer_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_footer_link()
        page.go_to_pricing_page_from_footer_link()

    def test_guest_can_go_to_faq_page_from_footer_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_footer_link()
        page.go_to_faq_page_from_footer_link()

    def test_guest_can_go_to_learn_page_from_footer_link(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_footer_link()
        page.go_to_learn_page_from_footer_link()

    def test_guest_can_go_to_privacy_policy_page(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.go_to_privacy_policy_from_footer_link()


class TestContactUsEmailAddressField(BaseTest):

    def test_guest_cant_send_message_without_filling_email_address_field(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.is_email_address_field_required()

    def test_guest_can_enter_data(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_email_address_field(TestData.generate_valid_email_address())

    def test_guest_can_clear_data(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_email_address_field(TestData.generate_valid_email_address())
        page.clear_data_email_address_field()

    def test_guest_can_edit_entered_data(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_email_address_field(TestData.generate_valid_email_address())
        page.clear_data_email_address_field()
        page.enter_data_email_address_field(TestData.generate_valid_email_address())


class TestContactUsFirstNameField(BaseTest):
    def test_guest_can_send_message_without_filling_first_name(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_email_address_field(TestData.generate_valid_email_address())
        page.enter_data_message_field(TestData.generate_sentences(10))
        page.click_send_message_button()

    def test_guest_can_send_message_all_field_filled(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_first_name_field(TestData.generate_first_name())
        page.enter_data_email_address_field(TestData.generate_valid_email_address())
        page.enter_data_message_field(TestData.generate_sentences(10))
        page.click_send_message_button()

    def test_guest_can_enter_lowercase_letter(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_first_name_field(TestData.generate_random_characters(TestData.MAX_CHARACTER_FIRST_NAME_FIELD,
                                                                             TestData.LOWERCASE_LETTERS))

    def test_guest_can_enter_uppercase_letter(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_first_name_field(TestData.generate_random_characters(TestData.MAX_CHARACTER_FIRST_NAME_FIELD,
                                                                             TestData.UPPERCASE_LETTERS))

    def test_guest_can_enter_digits(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_first_name_field(TestData.generate_random_characters(TestData.MAX_CHARACTER_FIRST_NAME_FIELD,
                                                                             TestData.DIGITS))

    @pytest.mark.smoke
    def test_guest_can_enter_special_characters(self):
        page = ContactUsPage(self.driver)
        page.go_to_contact_us_page_from_header_link()
        page.enter_data_first_name_field(TestData.generate_random_characters(TestData.MAX_CHARACTER_FIRST_NAME_FIELD,
                                                                             TestData.PUNCTUATION))







