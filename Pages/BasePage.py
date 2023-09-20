import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.locators import BasePageLocators

"""This class is a parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # def clear(self, locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     return element.clear()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element

    def find_element(self, how, what):
        return self.driver.find_element(how, what)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def get_title(self):
        return self.driver.title

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

    def scroll(self, how, what):
        element = self.driver.find_element(how, what)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_signup_button_exist(self):
        assert self.is_element_present(*BasePageLocators.SIGNUP_BUTTON), "Sign Up button is not presented"

    def is_header_visible(self):
        assert self.is_element_present(*BasePageLocators.HEADER), "Header is not presented"

    def is_footer_visible(self):
        assert self.is_element_present(*BasePageLocators.FOOTER), "Footer is not presented"

    def is_header_logo_visible(self):
        assert self.is_element_present(*BasePageLocators.HEADER_LOGO), "Header logo is not presented"

    def is_get_free_views_visible(self):
        assert self.is_element_present(*BasePageLocators.GET_FREE_VIEWS), "Get free views is not presented"

    def go_to_home_page_from_header_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.HOME_LINK_HEADER)
        expected_link_name = "Home"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.HOME_LINK_HEADER)
        title = self.get_title()
        assert title == TestData.HOME_PAGE_TITLE, "Title of the Home page doesn't match"

    def go_to_pricing_page_from_header_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.PRICING_LINK_HEADER)
        expected_link_name = "Pricing"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.PRICING_LINK_HEADER)
        title = self.get_title()
        assert title == TestData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_faq_page_from_header_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.FAQ_LINK_HEADER)
        expected_link_name = "FAQ"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.FAQ_LINK_HEADER)
        title = self.get_title()
        assert title == TestData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def go_to_contact_us_page_from_header_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.CONTACT_US_LINK_HEADER)
        expected_link_name = "Contact Us"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.CONTACT_US_LINK_HEADER)
        title = self.get_title()
        assert title == TestData.CONTACT_US_PAGE_TITLE, "Title of the Contact Us page doesn't match"

    def go_to_learn_page_from_header_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.LEARN_LINK_HEADER)
        expected_link_name = "Learn"
        assert actual_link_name == expected_link_name, f"Name of the header Learn link doesn't match. " \
                                                       f"Expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.LEARN_LINK_HEADER)
        assert self.is_element_present(*BasePageLocators.LEARN_CONTAINER), "Learn container is not presented"

    def go_to_learn_page_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.LEARN_LINK_HEADER)
        expected_link_name = "Learn"
        assert actual_link_name == expected_link_name, f"Name of the footer Learn link doesn't match. " \
                                                       f"Expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.LEARN_LINK_FOOTER)
        assert self.is_element_present(*BasePageLocators.LEARN_CONTAINER), "Learn container is not presented"

    def go_to_home_page_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.HOME_LINK_FOOTER)
        expected_link_name = "Home"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.HOME_LINK_FOOTER)
        title = self.get_title()
        assert title == TestData.HOME_PAGE_TITLE, "Title of the Home page doesn't match"

    def go_to_pricing_page_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.PRICING_LINK_FOOTER)
        expected_link_name = "Pricing"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.PRICING_LINK_FOOTER)
        title = self.get_title()
        assert title == TestData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_faq_page_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.FAQ_LINK_FOOTER)
        expected_link_name = "FAQ"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.FAQ_LINK_FOOTER)
        title = self.get_title()
        assert title == TestData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def go_to_contact_us_page_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.CONTACT_US_LINK_FOOTER)
        expected_link_name = "Contact Us"
        assert actual_link_name == expected_link_name, f"expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.CONTACT_US_LINK_FOOTER)
        title = self.get_title()
        assert title == TestData.CONTACT_US_PAGE_TITLE, "Title of the Contact Us page doesn't match"

    def go_to_privacy_policy_from_footer_link(self):
        actual_link_name = self.get_element_text(BasePageLocators.PRIVACY_POLICY_LINK)
        expected_link_name = "Privacy Policy"
        assert actual_link_name == expected_link_name, f"Name of the Privacy Policy link doesn't match. " \
                                                       f"Expected {expected_link_name}, got {actual_link_name}"
        self.click(BasePageLocators.PRIVACY_POLICY_LINK)
        assert self.is_element_present(*BasePageLocators.PRIVACY_POLICY_CONTAINER), "Privacy Policy is not opened"




