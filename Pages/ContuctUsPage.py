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
        print(f"expected{TestData.CONTACT_US_PAGE_TITLE}, actual {title}")

    def is_contact_us_container_form_presented(self):
        actual_header = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_HEADER)
        expected_header = "GET IN TOUCH"
        actual_description = self.get_element_text(ContactUsPageLocators.GET_IN_TOUCH_DESCRIPTION)
        expected_description = "Have any questions? We'd love to hear from you"
        assert self.is_element_present(*ContactUsPageLocators.CONTACT_US_CONTAINER_FORM), "Contact Us container" \
                                                                                          " is not presented"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"
        assert actual_description == expected_description, f"expected {expected_description}, got {actual_description}"

