from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, HomePageLocators


class HomePage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    """Page Actions"""

    def check_home_page_title(self):
        title = self.get_title()
        assert title == TestData.HOME_PAGE_TITLE, "Title doesn't match"

    def is_boost_your_profile_container_presented(self):
        assert self.is_element_present(*HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_CONTAINER), "Boost your profile " \
                                                                                              "section is not presented"

    def is_what_do_we_offer_container_presented(self):
        assert self.is_element_present(*HomePageLocators.WHAT_DO_WE_OFFER_CONTAINER), "What do we offer " \
                                                                                              "section is not presented"

    def is_what_we_have_already_done_container_presented(self):
        assert self.is_element_present(*HomePageLocators.WHAT_WE_HAVE_ALREADY_DONE_CONTAINER), "What we have already done " \
                                                                                            "section is not presented"

    def is_promotion_formats_container_presented(self):
        assert self.is_element_present(*HomePageLocators.PROMOTION_FORMATS_CONTAINER), "Promotion formats " \
                                                                                            "section is not presented"

    def is_our_clients_trust_us_container_presented(self):
        assert self.is_element_present(*HomePageLocators.OUR_CLIENTS_TRUST_US_CONTAINER), "Promotion formats " \
                                                                                            "section is not presented"

    def is_any_questions_container_presented(self):
        assert self.is_element_present(*HomePageLocators.ANY_QUESTIONS_CONTAINER), "Any questions " \
                                                                                            "section is not presented"

