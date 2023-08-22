import time

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
        actual_text_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTIONS_HEADER)
        expected_text_first_question = "Is it safe to promote from you?"
        assert actual_text_first_question == expected_text_first_question, f"expected {expected_text_first_question}," \
                                                                           f" got {actual_text_first_question}"
        self.click(FaqPageLocators.FIRST_QUESTIONS_HEADER)
        actual_description_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTIONS_DESCRIPTION)
        expected_description_first_question = "Yap! We only request your username or the link to your TikTok profile." \
                                              " It is enough to boost your TikTok stats. We don't need your password," \
                                              " mail or anything else."
        assert actual_description_first_question == expected_description_first_question, f"expected " \
                                                                                         f"{expected_description_first_question}," \
                                                                                         f" got {actual_description_first_question}"


