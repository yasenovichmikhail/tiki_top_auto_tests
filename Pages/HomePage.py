import time

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

    def is_make_an_order_button_presented(self):
        actual_button_name = self.get_element_text(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        expected_button_name = "Make an order"
        assert self.is_element_present(*HomePageLocators.MAKE_AN_ORDER_BUTTON), "Make an order button is not presented"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"

    def is_how_it_works_button_presented(self):
        actual_button_name = self.get_element_text(HomePageLocators.HOW_IT_WORKS_BUTTON)
        expected_button_name = "How it works?"
        assert self.is_element_present(*HomePageLocators.HOW_IT_WORKS_BUTTON), "How it works button is not presented"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"

    def is_boost_your_profile_container_presented(self):
        assert self.is_element_present(*HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_CONTAINER), "Boost your profile " \
                                                                                              "section is not presented"
        actual_header = self.get_element_text(HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_HEADER)
        expected_header = "BOOST YOUR TIKTOK PROFILE & VIDEOS"
        actual_description = self.get_element_text(HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_DESCRIPTION)
        expected_description = "Promote your new video to get it into people's recommendations. " \
                               "Buy a subscription to keep your stats up to date. Become popular!"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"
        assert actual_description == expected_description, f"expected {expected_description}, got {actual_description}"

    def is_what_do_we_offer_container_presented(self):
        assert self.is_element_present(*HomePageLocators.WHAT_DO_WE_OFFER_CONTAINER), "What do we offer " \
                                                                                              "section is not presented"
        actual_header = self.get_element_text(HomePageLocators.WHAT_DO_WE_OFFER_HEADER)
        expected_header = "WHAT DO WE OFFER?"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"

    def is_what_we_have_already_done_container_presented(self):
        assert self.is_element_present(*HomePageLocators.WHAT_WE_HAVE_ALREADY_DONE_CONTAINER), "What we have already done " \
                                                                                            "section is not presented"
        actual_header = self.get_element_text(HomePageLocators.WHAT_WE_HAVE_ALREADY_DONE_HEADER)
        expected_header = "WHAT WE'VE ALREADY DONE"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"

    def is_promotion_formats_container_presented(self):
        assert self.is_element_present(*HomePageLocators.PROMOTION_FORMATS_CONTAINER), "Promotion formats " \
                                                                                            "section is not presented"
        actual_header = self.get_element_text(HomePageLocators.PROMOTION_FORMATS_HEADER)
        expected_header = "PROMOTION FORMATS"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"

    def is_our_clients_trust_us_container_presented(self):
        assert self.is_element_present(*HomePageLocators.OUR_CLIENTS_TRUST_US_CONTAINER), "Promotion formats " \
                                                                                            "section is not presented"
        actual_header = self.get_element_text(HomePageLocators.OUR_CLIENTS_TRUST_US_HEADER)
        expected_header = "OUR CLIENTS TRUST US"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"

    def is_any_questions_container_presented(self):
        actual_header = self.get_element_text(HomePageLocators.ANY_QUESTIONS_HEADER)
        expected_header = "ANY QUESTIONS?"
        actual_description = self.get_element_text(HomePageLocators.ANY_QUESTIONS_DESCRIPTION)
        expected_description = "Our services offer high-end promotion packages whose destiny is to power-up your" \
                               " TikTok presence. Boost to the element of your choice immediately —be it likes," \
                               " views, and whatnot."
        assert self.is_element_present(*HomePageLocators.ANY_QUESTIONS_CONTAINER), "Any questions " \
                                                                                   "section is not presented"
        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"
        assert actual_description == expected_description, f"expected {expected_description}, got {actual_description}"

    def go_to_pricing_page_from_boost_your_profile_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        expected_button_name = "Make an order"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"
        self.click(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        assert self.get_title() == TestData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_pricing_page_from_what_do_we_offer_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON)
        expected_button_name = "Get more info"
        assert actual_button_name in expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"
        self.click(HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON)
        assert self.get_title() == TestData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_pricing_page_from_promotion_formats_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON)
        expected_button_name = "Get more info"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"
        self.click(HomePageLocators.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON)
        assert self.get_title() == TestData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_faq_page_from_any_questions_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.ANY_QUESTIONS_MORE_INFO_BUTTON)
        expected_button_name = "More info"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"
        self.click(HomePageLocators.ANY_QUESTIONS_MORE_INFO_BUTTON)
        assert self.get_title() == TestData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def go_to_contact_us_page_from_any_questions_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.ANY_QUESTIONS_CONTACT_US_BUTTON)
        expected_button_name = "Contact us"
        assert actual_button_name == expected_button_name, f"expected {expected_button_name}, got {actual_button_name}"
        self.click(HomePageLocators.ANY_QUESTIONS_CONTACT_US_BUTTON)
        assert self.get_title() == TestData.CONTACT_US_PAGE_TITLE, "Title of the Contact us page doesn't match"

    def scroll_to_the_object(self):
        self.scroll(*HomePageLocators.ANY_QUESTIONS_CONTAINER)


