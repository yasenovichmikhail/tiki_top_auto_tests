import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData, FaqTestData
from Pages.BasePage import BasePage
from Pages.locators import BasePageLocators, HomePageLocators, FaqPageLocators


class FaqPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_faq_page_title(self):
        title = self.get_title()
        assert title == FaqTestData.FAQ_PAGE_TITLE, "Title of the FAQ page doesn't match"

    def is_popular_questions_container_presented(self):
        self.is_element_present(*FaqPageLocators.POPULAR_QUESTIONS_CONTAINER)
        actual_header = self.get_element_text(FaqPageLocators.POPULAR_QUESTIONS_HEADER)

        assert actual_header == FaqTestData.POPULAR_QUESTIONS_HEADER, \
            f"Expected {FaqTestData.POPULAR_QUESTIONS_HEADER}, got {actual_header}"

    def expand_first_question(self):
        actual_text_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTION_HEADER)
        self.click(FaqPageLocators.FIRST_QUESTION_HEADER)
        actual_description_first_question = self.get_element_text(FaqPageLocators.FIRST_QUESTION_DESCRIPTION)
        assert actual_text_first_question == FaqTestData.FIRST_QUESTION_HEADER, \
            f"Expected {FaqTestData.FIRST_QUESTION_HEADER}, got {actual_text_first_question}"
        assert actual_description_first_question == FaqTestData.FIRST_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.FIRST_QUESTION_DESCRIPTION}, got {actual_description_first_question}"

    def collapse_first_question(self):
        self.click(FaqPageLocators.FIRST_QUESTION_HEADER)

    def expand_second_question(self):
        actual_text_second_question = self.get_element_text(FaqPageLocators.SECOND_QUESTION_HEADER)
        self.click(FaqPageLocators.SECOND_QUESTION_HEADER)
        actual_description_second_question = self.get_element_text(FaqPageLocators.SECOND_QUESTION_DESCRIPTION)
        assert actual_text_second_question == FaqTestData.SECOND_QUESTION_HEADER,\
            f"Expected {FaqTestData.SECOND_QUESTION_HEADER}, got {actual_text_second_question}"
        assert actual_description_second_question == FaqTestData.SECOND_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.SECOND_QUESTION_DESCRIPTION}, got {actual_description_second_question}"

    def collapse_second_question(self):
        self.click(FaqPageLocators.SECOND_QUESTION_HEADER)

    def expand_third_question(self):
        actual_text_third_question = self.get_element_text(FaqPageLocators.THIRD_QUESTION_HEADER)
        self.click(FaqPageLocators.THIRD_QUESTION_HEADER)
        actual_description_third_question = self.get_element_text(FaqPageLocators.THIRD_QUESTION_DESCRIPTION)
        assert actual_text_third_question == FaqTestData.THIRD_QUESTION_HEADER,\
            f"Expected {FaqTestData.THIRD_QUESTION_HEADER}, got {actual_text_third_question}"
        assert actual_description_third_question == FaqTestData.THIRD_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.THIRD_QUESTION_DESCRIPTION}, got {actual_description_third_question}"

    def collapse_third_question(self):
        self.click(FaqPageLocators.THIRD_QUESTION_HEADER)

    def expand_fourth_question(self):
        actual_text_fourth_question = self.get_element_text(FaqPageLocators.FOURTH_QUESTION_HEADER)
        self.click(FaqPageLocators.FOURTH_QUESTION_HEADER)
        actual_description_fourth_question = self.get_element_text(FaqPageLocators.FOURTH_QUESTION_DESCRIPTION)
        assert actual_text_fourth_question == FaqTestData.FOURTH_QUESTION_HEADER,\
            f"Expected {FaqTestData.FOURTH_QUESTION_HEADER}, got {actual_text_fourth_question}"
        assert actual_description_fourth_question == FaqTestData.FOURTH_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.FOURTH_QUESTION_DESCRIPTION}, got {actual_description_fourth_question}"

    def collapse_fourth_question(self):
        self.click(FaqPageLocators.FOURTH_QUESTION_HEADER)

    def expand_fifth_question(self):
        actual_text_fifth_question = self.get_element_text(FaqPageLocators.FIFTH_QUESTION_HEADER)
        self.click(FaqPageLocators.FIFTH_QUESTION_HEADER)
        actual_description_fifth_question = self.get_element_text(FaqPageLocators.FIFTH_QUESTION_DESCRIPTION)
        assert actual_text_fifth_question == FaqTestData.FIFTH_QUESTION_HEADER,\
            f"Expected {FaqTestData.FIFTH_QUESTION_HEADER}, got {actual_text_fifth_question}"
        assert actual_description_fifth_question == FaqTestData.FIFTH_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.FIFTH_QUESTION_DESCRIPTION}, got {actual_description_fifth_question}"

    def collapse_fifth_question(self):
        self.click(FaqPageLocators.FIFTH_QUESTION_HEADER)

    def expand_sixth_question(self):
        actual_text_sixth_question = self.get_element_text(FaqPageLocators.SIXTH_QUESTION_HEADER)
        self.click(FaqPageLocators.SIXTH_QUESTION_HEADER)
        actual_description_sixth_question = self.get_element_text(FaqPageLocators.SIXTH_QUESTION_DESCRIPTION)
        assert actual_text_sixth_question == FaqTestData.SIXTH_QUESTION_HEADER,\
            f"Expected {FaqTestData.SIXTH_QUESTION_HEADER}, got {actual_text_sixth_question}"
        assert actual_description_sixth_question == FaqTestData.SIXTH_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.SIXTH_QUESTION_DESCRIPTION}, got {actual_description_sixth_question}"

    def collapse_sixth_question(self):
        self.click(FaqPageLocators.SIXTH_QUESTION_HEADER)

    def expand_seventh_question(self):
        actual_text_seventh_question = self.get_element_text(FaqPageLocators.SEVENTH_QUESTION_HEADER)
        self.click(FaqPageLocators.SEVENTH_QUESTION_HEADER)
        actual_description_seventh_question = self.get_element_text(FaqPageLocators.SEVENTH_QUESTION_DESCRIPTION)
        assert actual_text_seventh_question == FaqTestData.SEVENTH_QUESTION_HEADER,\
            f"Expected {FaqTestData.SEVENTH_QUESTION_HEADER}, got {actual_text_seventh_question}"
        assert actual_description_seventh_question == FaqTestData.SEVENTH_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.SEVENTH_QUESTION_DESCRIPTION}, got {actual_description_seventh_question}"

    def collapse_seventh_question(self):
        self.click(FaqPageLocators.SEVENTH_QUESTION_HEADER)

    def expand_eighth_question(self):
        actual_text_eighth_question = self.get_element_text(FaqPageLocators.EIGHTH_QUESTION_HEADER)
        self.click(FaqPageLocators.EIGHTH_QUESTION_HEADER)
        actual_description_eighth_question = self.get_element_text(FaqPageLocators.EIGHTH_QUESTION_DESCRIPTION)
        assert actual_text_eighth_question == FaqTestData.EIGHTH_QUESTION_HEADER,\
            f"Expected {FaqTestData.EIGHTH_QUESTION_HEADER}, got {actual_text_eighth_question}"
        assert actual_description_eighth_question == FaqTestData.EIGHTH_QUESTION_DESCRIPTION,\
            f"Expected {FaqTestData.EIGHTH_QUESTION_DESCRIPTION}, got {actual_description_eighth_question}"

    def collapse_eighth_question(self):
        self.click(FaqPageLocators.EIGHTH_QUESTION_HEADER)





