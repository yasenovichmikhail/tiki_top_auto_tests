import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, HomePageLocators, FaqPageLocators


class FaqPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_faq_page_title(self):
        title = self.get_title()
        assert title == TestData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def is_popular_questions_container_presented(self):
        self.is_element_present(*FaqPageLocators.POPULAR_QUESTIONS_CONTAINER)
        actual_header = self.get_element_text(FaqPageLocators.POPULAR_QUESTIONS_HEADER)
        expected_header = "POPULAR QUESTIONS"

        assert actual_header == expected_header, f"expected {expected_header}, got {actual_header}"

    def expand_first_question(self):
        actual_text_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTION_HEADER)
        expected_text_first_question = "Is it safe to promote from you?"
        assert actual_text_first_question == expected_text_first_question, f"expected {expected_text_first_question}," \
                                                                           f" got {actual_text_first_question}"
        self.click(FaqPageLocators.FIRST_QUESTION_HEADER)
        actual_description_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTION_DESCRIPTION)
        expected_description_first_question = "Yap! We only request your username or the link to your TikTok profile." \
                                              " It is enough to boost your TikTok stats. We don't need your password," \
                                              " mail or anything else."

        assert actual_description_first_question == expected_description_first_question,\
            f"expected {expected_description_first_question}, got {actual_description_first_question}"

    def collapse_first_question(self):
        self.click(FaqPageLocators.FIRST_QUESTION_HEADER)

    def expand_second_question(self):
        actual_text_second_question = self.get_element_text(FaqPageLocators.SECOND_QUESTION_HEADER)
        expected_text_second_question = "What are the promotion limits?"

        assert actual_text_second_question == expected_text_second_question,\
            f"expected {expected_text_second_question}, got {actual_text_second_question}"

        self.click(FaqPageLocators.SECOND_QUESTION_HEADER)
        actual_description_second_question = self.get_element_text(FaqPageLocators.SECOND_QUESTION_DESCRIPTION)
        expected_description_second_question = "The limit is the maximum number on the Pricing page." \
                                               " This is due to our capacity, we strive to make the limit higher."

        assert actual_description_second_question == expected_description_second_question,\
            f"expected {expected_description_second_question}, got {actual_description_second_question}"

    def collapse_second_question(self):
        self.click(FaqPageLocators.SECOND_QUESTION_HEADER)

    def expand_third_question(self):
        actual_text_third_question = self.get_element_text(FaqPageLocators.THIRD_QUESTION_HEADER)
        expected_text_third_question = "What are the accepted payment methods?"

        assert actual_text_third_question == expected_text_third_question,\
            f"expected {expected_text_third_question}, got {actual_text_third_question}"

        self.click(FaqPageLocators.THIRD_QUESTION_HEADER)
        actual_description_third_question = self.get_element_text(FaqPageLocators.THIRD_QUESTION_DESCRIPTION)
        expected_description_third_question = "Now you can pay with credit/debit card through Stripe only. However," \
                                              " we are working on having multiple payment methods for later on."

        assert actual_description_third_question == expected_description_third_question,\
            f"expected {expected_description_third_question}, got {actual_description_third_question}"

    def collapse_third_question(self):
        self.click(FaqPageLocators.THIRD_QUESTION_HEADER)

    def expand_fourth_question(self):
        actual_text_fourth_question = self.get_element_text(FaqPageLocators.FOURTH_QUESTION_HEADER)
        expected_text_fourth_question = "Can I promote someone else's account?"

        assert actual_text_fourth_question == expected_text_fourth_question,\
            f"expected {expected_text_fourth_question}, got {actual_text_fourth_question}"

        self.click(FaqPageLocators.FOURTH_QUESTION_HEADER)
        actual_description_fourth_question = self.get_element_text(FaqPageLocators.FOURTH_QUESTION_DESCRIPTION)
        expected_description_fourth_question = "Yes, you need only a username or the link to someone else’s account."

        assert actual_description_fourth_question == expected_description_fourth_question,\
            f"expected {expected_description_fourth_question}, got {actual_description_fourth_question}"

    def collapse_fourth_question(self):
        self.click(FaqPageLocators.FOURTH_QUESTION_HEADER)

    def expand_fifth_question(self):
        actual_text_fifth_question = self.get_element_text(FaqPageLocators.FIFTH_QUESTION_HEADER)
        expected_text_fifth_question = "What is Order?"

        assert actual_text_fifth_question == expected_text_fifth_question,\
            f"expected {expected_text_fifth_question}, got {actual_text_fifth_question}"

        self.click(FaqPageLocators.FIFTH_QUESTION_HEADER)
        actual_description_fifth_question = self.get_element_text(FaqPageLocators.FIFTH_QUESTION_DESCRIPTION)
        expected_description_fifth_question = "Order is promotion of one category per post."

        assert actual_description_fifth_question == expected_description_fifth_question,\
            f"expected {expected_description_fifth_question}, got {actual_description_fifth_question}"

    def collapse_fifth_question(self):
        self.click(FaqPageLocators.FIFTH_QUESTION_HEADER)

    def expand_sixth_question(self):
        actual_text_sixth_question = self.get_element_text(FaqPageLocators.SIXTH_QUESTION_HEADER)
        expected_text_sixth_question = "What number of days is better to choose for an order?"

        assert actual_text_sixth_question == expected_text_sixth_question,\
            f"expected {expected_text_sixth_question}, got {actual_text_sixth_question}"

        self.click(FaqPageLocators.SIXTH_QUESTION_HEADER)
        actual_description_sixth_question = self.get_element_text(FaqPageLocators.SIXTH_QUESTION_DESCRIPTION)
        expected_description_sixth_question = "The more days you choose, the bigger chance that we can boost your" \
                                              " account evenly so as not to arouse suspicion for TikTok. Otherwise," \
                                              " your account can be banned or suspended by TikTok."

        assert actual_description_sixth_question == expected_description_sixth_question,\
            f"expected {expected_description_sixth_question}, got {actual_description_sixth_question}"

    def collapse_sixth_question(self):
        self.click(FaqPageLocators.SIXTH_QUESTION_HEADER)

    def expand_seventh_question(self):
        actual_text_seventh_question = self.get_element_text(FaqPageLocators.SEVENTH_QUESTION_HEADER)
        expected_text_seventh_question = "How to stop an active order?"

        assert actual_text_seventh_question == expected_text_seventh_question,\
            f"expected {expected_text_seventh_question}, got {actual_text_seventh_question}"

        self.click(FaqPageLocators.SEVENTH_QUESTION_HEADER)
        actual_description_seventh_question = self.get_element_text(FaqPageLocators.SEVENTH_QUESTION_DESCRIPTION)
        expected_description_seventh_question = "If you want to stop an active order, you can delete it but you " \
                                                "should know that your money won't be refunded. Steps to delete an " \
                                                "order: My Profile ➝ Order ➝ Delete Order."

        assert actual_description_seventh_question == expected_description_seventh_question,\
            f"expected {expected_description_seventh_question}, got {actual_description_seventh_question}"

    def collapse_seventh_question(self):
        self.click(FaqPageLocators.SEVENTH_QUESTION_HEADER)

    def expand_eighth_question(self):
        actual_text_eighth_question = self.get_element_text(FaqPageLocators.EIGHTH_QUESTION_HEADER)
        expected_text_eighth_question = "Can I do multiple orders on 1 post?"

        assert actual_text_eighth_question == expected_text_eighth_question,\
            f"expected {expected_text_eighth_question}, got {actual_text_eighth_question}"

        self.click(FaqPageLocators.EIGHTH_QUESTION_HEADER)
        actual_description_eighth_question = self.get_element_text(FaqPageLocators.EIGHTH_QUESTION_DESCRIPTION)
        expected_description_eighth_question = "Yes, you can, but you have to do it with different categories."

        assert actual_description_eighth_question == expected_description_eighth_question,\
            f"expected {expected_description_eighth_question}, got {actual_description_eighth_question}"

    def collapse_eighth_question(self):
        self.click(FaqPageLocators.EIGHTH_QUESTION_HEADER)





