import random
import time

import pytest
from selenium.webdriver.common.by import By

import Config.config
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, HomePageLocators, FaqPageLocators, ContactUsPageLocators


class ContactUsPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_contact_us_page_title(self):
        title = self.get_title()
        assert title == TestData.CONTACT_US_PAGE_TITLE, "Title of the Contact Us page doesn't match"

    def is_contact_us_container_form_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_HEADER)
        expected_header = "GET IN TOUCH"
        actual_description = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_DESCRIPTION)
        expected_description = "Have any questions? We'd love to hear from you"
        assert self.is_element_present(*ContactUsPageLocators.CONTACT_US_CONTAINER_FORM), "Contact Us container" \
                                                                                          " is not presented"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"
        assert actual_description == expected_description, f"expected {expected_description}, got {actual_description}"

    def is_first_name_text_field_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.FIRST_NAME_TEXT_FIELD_HEADER)
        expected_header = "First name"
        assert self.is_element_present(*ContactUsPageLocators.FIRST_NAME_TEXT_FIELD), "First name text field" \
                                                                                      " is not presented"
        assert actual_header == expected_header, f"Header of the first name text field doesn't match." \
                                                 f" Expected {expected_header}, got {actual_header}"

    def is_first_name_text_field_placeholder_presented(self):
        text_field = self.find_element(*ContactUsPageLocators.FIRST_NAME_TEXT_FIELD)
        actual_placeholder = text_field.get_attribute('placeholder')
        expected_placeholder = "Ex: Paul, Kate, John"
        assert actual_placeholder == expected_placeholder, f"Placeholder of the first name text field doesn't match." \
                                                           f" Expected {expected_placeholder}, got {actual_placeholder}"

    def is_email_address_text_field_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD_HEADER)
        expected_header = "Email address"
        assert self.is_element_present(*ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD), "Email address text field" \
                                                                                         " is not presented"
        assert actual_header == expected_header, f"Header of the email address text field doesn't match." \
                                                 f" Expected {expected_header}, got {actual_header}"

    def is_email_address_text_field_placeholder_presented(self):
        text_field = self.find_element(*ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_placeholder = text_field.get_attribute('placeholder')
        expected_placeholder = "tikitop.team@gmail.com"
        assert actual_placeholder == expected_placeholder, f"Placeholder of the email address text field doesn't" \
                                                           f" match. Expected {expected_placeholder}," \
                                                           f" got {actual_placeholder}"

    def is_message_text_area_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.MESSAGE_TEXT_AREA_HEADER)
        expected_header = "Message"
        assert self.is_element_present(*ContactUsPageLocators.MESSAGE_TEXT_AREA), "Message text field is not presented"
        assert actual_header == expected_header, f"Header of the message text field doesn't match." \
                                                 f" Expected {expected_header}, got {actual_header}"

    def is_message_text_area_placeholder_presented(self):
        text_area = self.find_element(*ContactUsPageLocators.MESSAGE_TEXT_AREA)
        actual_placeholder = text_area.get_attribute('placeholder')
        expected_placeholder = "Hello! I would like to ask you about..."
        assert actual_placeholder == expected_placeholder, f"Placeholder of the message text area doesn't" \
                                                           f" match. Expected {expected_placeholder}," \
                                                           f" got {actual_placeholder}"

    def is_send_message_button_presented(self):
        actual_button_name = self.get_element_text(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        expected_button_name = "Send message"
        assert self.is_element_present(*ContactUsPageLocators.SEND_MESSAGE_BUTTON), "Send message button " \
                                                                                    "is not presented"
        assert actual_button_name == expected_button_name, f"Name of the send message button doesn't match. " \
                                                           f"Expected {expected_button_name}, got {actual_button_name}"

    def is_privacy_policy_button_presented(self):
        actual_button_name = self.get_element_text(ContactUsPageLocators.PRIVACY_POLICY_BUTTON)
        expected_button_name = "Privacy Policy"
        assert self.is_element_present(*ContactUsPageLocators.PRIVACY_POLICY_BUTTON), "Privacy Policy button is " \
                                                                                      "not presented"
        assert actual_button_name == expected_button_name, f"Name of the Privacy Policy button doesn't match. " \
                                                           f"Expected {expected_button_name}, got {actual_button_name}"

    def is_privacy_policy_opened(self):
        self.click(ContactUsPageLocators.PRIVACY_POLICY_BUTTON)
        actual_header = self.get_element_text(BasePageLocators.PRIVACY_POLICY_HEADER)
        expected_header = "PRIVACY POLICY"
        assert self.is_element_present(*BasePageLocators.PRIVACY_POLICY_CONTAINER), "Privacy Policy is not opened"
        assert actual_header == expected_header, f"Header of the Privacy Policy doesn't match. " \
                                                 f"Expected {expected_header}, got {actual_header}"

    def is_email_address_field_required(self):
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        actual_warning = self.get_element_text(ContactUsPageLocators.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING)
        expected_warning = "Required"
        assert self.is_element_present(*ContactUsPageLocators.EMAIL_ADDRESS_FIELD_REQUIRED_WARNING), "Warning is" \
                                                                                                     " not presented"
        assert actual_warning == expected_warning, f"Warning of the empty email address field doesn't match. " \
                                                   f"Expected {expected_warning}, got {actual_warning}"

    def enter_data_email_address_field(self):
        self.send_keys(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD, TestData.generate_valid_email_address())
        email_address_field = self.find_element(*ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_value = email_address_field.get_attribute('value')
        assert len(actual_value) > 0, "Data is not entered"
        time.sleep(5)

    def clear_data_email_address_field(self):
        email_address_field = self.find_element(*ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD)
        actual_value = email_address_field.get_attribute('value')
        # print(f"actual_value is {actual_value}")
        email_address_field.clear()
        actual_value1 = email_address_field.get_attribute('value')
        # print(f"actual_value_new is {actual_value1}")








    def is_message_field_required(self):
        self.click(ContactUsPageLocators.SEND_MESSAGE_BUTTON)
        actual_warning = self.get_element_text(ContactUsPageLocators.MESSAGE_TEXT_AREA_REQUIRED_WARNING)
        expected_warning = "Required"
        assert self.is_element_present(*ContactUsPageLocators.MESSAGE_TEXT_AREA_REQUIRED_WARNING), "Warning is" \
                                                                                                     " not presented"
        assert actual_warning == expected_warning, f"Warning of the empty message field doesn't match. " \
                                                   f"Expected {expected_warning}, got {actual_warning}"



