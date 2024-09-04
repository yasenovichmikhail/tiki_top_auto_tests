import time

from Config.config import PricingPageData
from Pages.BasePage import BasePage
from Pages.locators import PricingPageLocators
from selenium.webdriver.common.by import By


class PricingPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_pricing_page_title(self):
        title = self.get_title()
        assert title == PricingPageData.PRICING_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def choose_likes(self):
        self.click(PricingPageLocators.LIKES_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of likes"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def choose_views(self):
        self.click(PricingPageLocators.VIEWS_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of views"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def choose_followers(self):
        self.click(PricingPageLocators.FOLLOWERS_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of followers"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def choose_comments(self):
        self.click(PricingPageLocators.COMMENTS_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of comments"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def choose_reposts(self):
        self.click(PricingPageLocators.REPOSTS_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of reposts"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    def increase_number(self, num):
        for i in range(num):
            self.click(PricingPageLocators.INCREASE_NUMBER_BUTTON)
            time.sleep(2)

    def decrease_number(self, num):
        for i in range(num):
            self.click(PricingPageLocators.DECREASE_NUMBER_BUTTON)
            time.sleep(2)

    def enter_number_manually(self, num):
        self.click(PricingPageLocators.INPUT_NUMBER_FIELD)
        self.send_keys(PricingPageLocators.INPUT_NUMBER_FIELD, num)
        time.sleep(3)
