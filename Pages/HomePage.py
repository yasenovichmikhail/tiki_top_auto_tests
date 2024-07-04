import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData, ContactUsPageData, HomePageData, PricingPageData, FaqPageData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, HomePageLocators


class HomePage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def check_home_page_title(self):
        title = self.get_title()
        assert title == HomePageData.HOME_PAGE_TITLE, "Title doesn't match"

    def is_boost_your_profile_container_presented(self):
        assert self.is_element_present(HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_CONTAINER), \
            "Boost your profile container is not presented"
        actual_header = self.get_element_text(HomePageLocators.BOOST_YOUR_TIKTOK_PROFILE_HEADER)
        assert actual_header == HomePageData.BOOST_YOUR_TIKTOK_PROFILE_HEADER, \
            f"Expected {HomePageData.BOOST_YOUR_TIKTOK_PROFILE_HEADER}, got {actual_header}"

    def is_make_an_order_button_presented(self):
        actual_button_name = self.get_element_text(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        assert self.is_element_present(HomePageLocators.MAKE_AN_ORDER_BUTTON), "Make an order button is not presented"
        assert actual_button_name == HomePageData.MAKE_AN_ORDER_BUTTON, \
            f"Expected {HomePageData.MAKE_AN_ORDER_BUTTON}, got {actual_button_name}"

    def is_how_it_works_button_presented(self):
        actual_button_name = self.get_element_text(HomePageLocators.HOW_IT_WORKS_BUTTON)
        assert self.is_element_present(HomePageLocators.HOW_IT_WORKS_BUTTON), "How it works button is not presented"
        assert actual_button_name == HomePageData.HOW_IT_WORKS_BUTTON, \
            f"Expected {HomePageData.HOW_IT_WORKS_BUTTON}, got {actual_button_name}"

    def is_what_do_we_offer_container_presented(self):
        assert self.is_element_present(HomePageLocators.WHAT_DO_WE_OFFER_CONTAINER), \
            "What do we offer container is not presented"
        actual_header = self.get_element_text(HomePageLocators.WHAT_DO_WE_OFFER_HEADER)
        assert actual_header == HomePageData.WHAT_DO_WE_OFFER_CONTAINER_HEADER, \
            f"Expected {HomePageData.WHAT_DO_WE_OFFER_CONTAINER_HEADER}, got {actual_header}"

    def is_what_we_have_already_done_container_presented(self):
        assert self.is_element_present(HomePageLocators.WHAT_WE_HAVE_ALREADY_DONE_CONTAINER), \
            "What we have already done container is not presented"
        actual_header = self.get_element_text(HomePageLocators.WHAT_WE_HAVE_ALREADY_DONE_HEADER)
        assert actual_header == HomePageData.WHAT_WE_HAVE_DONE_CONTAINER_HEADER, \
            f"Expected {HomePageData.WHAT_WE_HAVE_DONE_CONTAINER_HEADER}, got {actual_header}"

    def is_promotion_formats_container_presented(self):
        assert self.is_element_present(HomePageLocators.PROMOTION_FORMATS_CONTAINER), \
            "Promotion formats container is not presented"
        actual_header = self.get_element_text(HomePageLocators.PROMOTION_FORMATS_HEADER)
        assert actual_header == HomePageData.PROMOTION_FORMATS_CONTAINER_HEADER, \
            f"Expected {HomePageData.PROMOTION_FORMATS_CONTAINER_HEADER}, got {actual_header}"

    def is_our_clients_trust_us_container_presented(self):
        assert self.is_element_present(HomePageLocators.OUR_CLIENTS_TRUST_US_CONTAINER), \
            "Promotion formats container is not presented"
        actual_header = self.get_element_text(HomePageLocators.OUR_CLIENTS_TRUST_US_HEADER)
        assert actual_header == HomePageData.OUR_CLIENTS_TRUST_US_CONTAINER_HEADER, \
            f"Expected {HomePageData.OUR_CLIENTS_TRUST_US_CONTAINER_HEADER}, got {actual_header}"

    def is_any_questions_container_presented(self):
        assert self.is_element_present(HomePageLocators.ANY_QUESTIONS_CONTAINER), \
            f"Any questions container is not presented"
        actual_header = self.get_element_text(HomePageLocators.ANY_QUESTIONS_HEADER)
        actual_description = self.get_element_text(HomePageLocators.ANY_QUESTIONS_DESCRIPTION)
        assert actual_header == HomePageData.ANY_QUESTIONS_CONTAINER_HEADER, \
            f"Expected {HomePageData.ANY_QUESTIONS_CONTAINER_HEADER}, got {actual_header}"
        assert actual_description == HomePageData.ANY_QUESTIONS_DESCRIPTION, \
            f"Expected {HomePageData.ANY_QUESTIONS_DESCRIPTION}, got {actual_description}"

    def go_to_pricing_page_from_boost_your_profile_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        assert actual_button_name == HomePageData.MAKE_AN_ORDER_BUTTON, \
            f"Expected {HomePageData.MAKE_AN_ORDER_BUTTON}, got {actual_button_name}"
        self.click(HomePageLocators.MAKE_AN_ORDER_BUTTON)
        assert self.get_title() == PricingPageData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_pricing_page_from_what_do_we_offer_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON)
        assert actual_button_name in HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON, \
            f"Expected {HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON}, got {actual_button_name}"
        self.click(HomePageLocators.WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON)
        assert self.get_title() == PricingPageData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_pricing_page_from_promotion_formats_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON)
        assert actual_button_name == HomePageData.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON, \
            f"Expected {HomePageData.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON}, got {actual_button_name}"
        self.click(HomePageLocators.PROMOTION_FORMATS_GET_MORE_INFO_BUTTON)
        assert self.get_title() == PricingPageData.PRICING_PAGE_TITLE, "Title of the Pricing page doesn't match"

    def go_to_faq_page_from_any_questions_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.ANY_QUESTIONS_MORE_INFO_BUTTON)
        assert actual_button_name == HomePageData.ANY_QUESTIONS_MORE_INFO_BUTTON, \
            f"Expected {HomePageData.ANY_QUESTIONS_MORE_INFO_BUTTON}, got {actual_button_name}"
        self.click(HomePageLocators.ANY_QUESTIONS_MORE_INFO_BUTTON)
        assert self.get_title() == FaqPageData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def go_to_contact_us_page_from_any_questions_section(self):
        actual_button_name = self.get_element_text(HomePageLocators.ANY_QUESTIONS_CONTACT_US_BUTTON)
        assert actual_button_name == HomePageData.ANY_QUESTIONS_CONTACT_US_BUTTON, \
            f"Expected {HomePageData.ANY_QUESTIONS_CONTACT_US_BUTTON}, got {actual_button_name}"
        self.click(HomePageLocators.ANY_QUESTIONS_CONTACT_US_BUTTON)
        assert self.get_title() == ContactUsPageData.CONTACT_US_PAGE_TITLE, "Title of the Contact us page doesn't match"


