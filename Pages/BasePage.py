from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_title(self):
        return self.driver.title

    def is_signup_button_exist(self):
        assert self.is_element_present(*BasePageLocators.SIGNUP_BUTTON), "Sign Up button is not presented"

    def is_header_visible(self):
        assert self.is_element_present(*BasePageLocators.HEADER), "Header is not presented"

    def is_footer_visible(self):
        assert self.is_element_present(*BasePageLocators.FOOTER), "Footer is not presented"

    def is_header_logo_visible(self):
        logo = self.is_element_present(*BasePageLocators.HEADER_LOGO)
        assert logo, "Header logo is not presented"
