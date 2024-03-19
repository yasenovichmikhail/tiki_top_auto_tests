import random
import time

import pytest
from selenium.webdriver.common.by import By

import Config.config
from Config.config import TestData, ContactUsPageData
from Pages.BasePage import BasePage
from Pages.locators import ContactUsPageLocators, BasePageLocators


class ContactUsPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_contact_us_page_title(self):
        title = self.get_title()
        assert title == ContactUsPageData.CONTACT_US_PAGE_TITLE, \
            f"Title of the Contact Us page doesn't match"

    def is_contact_us_container_form_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_HEADER)
        actual_description = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_DESCRIPTION)
        assert self.is_element_present(ContactUsPageLocators.CONTACT_US_CONTAINER_FORM), \
            f"Contact Us container is not presented"
        assert actual_header == ContactUsPageData.GET_IN_TOUCH_HEADER, \
            f"Header of the contact us container doesn't match. " \
            f"Expected {ContactUsPageData.GET_IN_TOUCH_HEADER}, got {actual_header}"
        assert actual_description == ContactUsPageData.GET_IN_TOUCH_DESCRIPTION, \
            f"Header of the contact us description doesn't match. " \
            f"Expected {ContactUsPageData.GET_IN_TOUCH_DESCRIPTION}, got {actual_description}"

    def is_first_name_text_field_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD_HEADER)
        assert self.is_element_present(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD), \
            "First name text field is not presented"
        assert actual_header == ContactUsPageData.FIRST_NAME_TEXT_FIELD_HEADER,\
            f"Header of the first name text field doesn't match. " \
            f" Expected {ContactUsPageData.FIRST_NAME_TEXT_FIELD_HEADER}, got {actual_header}"

    def is_first_name_text_field_placeholder_presented(self):
        text_field = self.find_element(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD)
        actual_placeholder = text_field.get_attribute('placeholder')
        assert actual_placeholder == ContactUsPageData.FIRST_NAME_FIELD_PLACEHOLDER, \
            f"Placeholder of the first name text field doesn't match. " \
            f"Expected {ContactUsPageData.FIRST_NAME_FIELD_PLACEHOLDER}, got {actual_placeholder}"

    def is_email_address_text_field_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD_HEADER)
        assert self.is_element_present(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD),\
            f"Email address text field is not presented"
        assert actual_header == ContactUsPageData.EMAIL_ADDRESS_TEXT_FIELD_HEADER,\
            f"Header of the email address text field doesn't match." \
            f" Expected {ContactUsPageData.EMAIL_ADDRESS_TEXT_FIELD_HEADER}, got {actual_header}"

    def is_email_address_text_field_placeholder_presented(self):
        text_field = self.find_element(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_placeholder = text_field.get_attribute('placeholder')
        assert actual_placeholder == ContactUsPageData.EMAIL_ADDRESS_FIELD_PLACEHOLDER,\
            f"Placeholder of the email address text field doesn't match. " \
            f"Expected {ContactUsPageData.EMAIL_ADDRESS_FIELD_PLACEHOLDER}," \
            f" got {actual_placeholder}"

    def is_message_text_area_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.MESSAGE_TEXT_AREA_HEADER)
        assert self.is_element_present(ContactUsPageLocators.MESSAGE_TEXT_AREA), \
            f"Message text field is not presented"
        assert actual_header == ContactUsPageData.MESSAGE_TEXT_AREA_HEADER,\
            f"Header of the message text field doesn't match. " \
            f" Expected {ContactUsPageData.MESSAGE_TEXT_AREA_HEADER}, got {actual_header}"

    def is_message_text_area_placeholder_presented(self):
        text_area = self.find_element(ContactUsPageLocators.MESSAGE_TEXT_AREA)
        actual_placeholder = text_area.get_attribute('placeholder')
        assert actual_placeholder == ContactUsPageData.MESSAGE_TEXT_AREA_PLACEHOLDER,\
            f"Placeholder of the message text area doesn't" \
            f" match. Expected {ContactUsPageData.MESSAGE_TEXT_AREA_PLACEHOLDER} got {actual_placeholder}"

    def is_privacy_policy_link_presented(self):
        actual_button_name = self.get_element_text(ContactUsPageLocators.PRIVACY_POLICY_BUTTON)
        assert self.is_element_present(ContactUsPageLocators.PRIVACY_POLICY_BUTTON), \
            "Privacy Policy button is not presented"
        assert actual_button_name == ContactUsPageData.PRIVACY_POLICY_BUTTON, \
            f"Name of the Privacy Policy button doesn't match. " \
            f"Expected {ContactUsPageData.PRIVACY_POLICY_BUTTON}, got {actual_button_name}"

    def is_privacy_policy_opened(self):
        self.click(ContactUsPageLocators.PRIVACY_POLICY_BUTTON)
        actual_header = self.get_element_text(ContactUsPageData.PRIVACY_POLICY_HEADER)
        assert self.is_element_present(BasePageLocators.PRIVACY_POLICY_CONTAINER), "Privacy Policy is not opened"
        assert actual_header == ContactUsPageData.PRIVACY_POLICY_HEADER, \
            f"Header of the Privacy Policy doesn't match. " \
            f"Expected {ContactUsPageData.PRIVACY_POLICY_HEADER}, got {actual_header}"

    def is_email_address_field_required(self):
        self.send_keys(ContactUsPageLocators.MESSAGE_TEXT_AREA, TestData.generate_sentences(7))
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        actual_warning = self.get_element_text(ContactUsPageLocators.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING)
        assert self.is_element_present(ContactUsPageLocators.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING), \
            "Warning is not presented"
        assert actual_warning == ContactUsPageData.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING, \
            f"Warning of the empty email address field doesn't match. " \
            f"Expected {ContactUsPageData.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING}, got {actual_warning}"

    def is_message_field_required(self):
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        actual_warning = self.get_element_text(ContactUsPageLocators.MESSAGE_TEXT_AREA_REQUIRED_WARNING)
        assert self.is_element_present(ContactUsPageLocators.MESSAGE_TEXT_AREA_REQUIRED_WARNING), \
            "Warning is not presented"
        assert actual_warning == ContactUsPageData.MESSAGE_FIELD_REQUIRED_WARNING, \
            f"Warning of the empty message field doesn't match. " \
            f"Expected {ContactUsPageData.MESSAGE_FIELD_REQUIRED_WARNING}, got {actual_warning}"

    def is_max_length_warning_first_name_field_presented(self):
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        assert self.is_element_present(ContactUsPageLocators.MAX_LENGTH_FIRST_NAME_FIELD_WARNING), \
            "Warning is not presented"
        actual_warning = self.get_element_text(ContactUsPageLocators.MAX_LENGTH_FIRST_NAME_FIELD_WARNING)
        assert actual_warning == ContactUsPageData.MAX_LENGTH_FIRST_NAME_FIELD_WARNING, \
            f"Warning doesn't match. Expected {ContactUsPageData.MAX_LENGTH_FIRST_NAME_FIELD_WARNING}," \
            f" got {actual_warning}"

    def is_max_length_warning_first_name_field_not_presented(self):
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        assert self.is_not_element_present(ContactUsPageLocators.MAX_LENGTH_FIRST_NAME_FIELD_WARNING), \
            "Warning is presented"

    # TO DO: def is_min_length_warning_message_field_presented(self):
    #     sel

    def enter_first_name_field(self, value):
        assert self.is_element_present(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD), \
            "First name text field is not presented"
        actual_header = self.get_element_text(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD_HEADER)
        assert actual_header == ContactUsPageData.FIRST_NAME_TEXT_FIELD_HEADER, \
            f"Header of the first name text field doesn't match. " \
            f"Expected {ContactUsPageData.FIRST_NAME_TEXT_FIELD_HEADER}, got {actual_header}"
        self.send_keys(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD, value)
        first_name_field = self.find_element(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD)
        actual_value = first_name_field.get_attribute('value')
        assert len(actual_value) > 0, "Data is not entered"

    def enter_email_address_field(self, value):
        self.send_keys(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD, value)
        email_address_field = self.find_element(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_value = email_address_field.get_attribute('value')
        assert len(actual_value) > 0, "Data is not entered"

    def enter_message_field(self, value):
        self.send_keys(ContactUsPageLocators.MESSAGE_TEXT_AREA, value)
        message_field = self.find_element(ContactUsPageLocators.MESSAGE_TEXT_AREA)
        actual_value = message_field.get_attribute('value')
        assert len(actual_value) > 0, "Data is not entered"

    def clear_first_name_field(self):
        first_name_field = self.find_element(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD)
        actual_email = first_name_field.get_attribute('value')
        actual_len = len(actual_email)
        self.clear_data(first_name_field, actual_len)
        actual_new_value = first_name_field.get_attribute('value')
        assert len(actual_new_value) == 0, "Data is not cleared"

    def clear_email_address_field(self):
        email_address_field = self.find_element(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_email = email_address_field.get_attribute('value')
        actual_len = len(actual_email)
        self.clear_data(email_address_field, actual_len)
        actual_new_value = email_address_field.get_attribute('value')
        assert len(actual_new_value) == 0, "Data is not cleared"

    def clear_message_field(self):
        message_field = self.find_element(ContactUsPageLocators.MESSAGE_TEXT_AREA)
        actual_email = message_field.get_attribute('value')
        actual_len = len(actual_email)
        self.clear_data(message_field, actual_len)
        actual_new_value = message_field.get_attribute('value')
        assert len(actual_new_value) == 0, "Data is not cleared"

    def click_send_message_button(self):
        assert self.is_element_present(ContactUsPageLocators.SEND_MESSAGE_BUTTON), \
            "Send message button is not presented"
        send_message_button = self.find_element(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()
        actual_button_name = self.get_element_text(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        assert actual_button_name == ContactUsPageData.SEND_MESSAGE_BUTTON, \
            f"Name of the send message button doesn't match. " \
            f"Expected {ContactUsPageData.SEND_MESSAGE_BUTTON}, got {actual_button_name}"

