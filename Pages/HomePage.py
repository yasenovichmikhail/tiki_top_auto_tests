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

