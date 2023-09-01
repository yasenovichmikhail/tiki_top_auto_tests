import time

import pytest
from selenium.webdriver.common.by import By

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
        assert self.is_element_present(ContactUsPageLocators.EMAIL_ADDRESS_TEXT_FIELD), "Email address text field" \
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
