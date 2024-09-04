from Config.config import TestData, ContactUsPageData, HomePageData, PricingPageData, FaqPageData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, PricingPageLocators


class PricingPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def check_pricing_page_title(self):
        title = self.get_title()
        assert title == PricingPageData.PRICING_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def choose_likes(self):
        self.click(PricingPageLocators.LIKES_BUTTON)
        actual_header = self.get_element_text(PricingPageLocators.CHOOSE_TYPE_OF_ACTIONS_HEADER)
        expected_header = "Number of likes"
        assert actual_header == expected_header, f"Expected {expected_header}, got {actual_header}"

    

