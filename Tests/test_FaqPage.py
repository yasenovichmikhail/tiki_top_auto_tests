import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.FaqPage import FaqPage


class TestFaq(BaseTest):

    def test_faq_page_title(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.check_faq_page_title()

    def test_guest_can_see_signup_button_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        time.sleep(5)
        page.is_signup_button_exist()

    def test_guest_can_see_header_logo_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_header_logo_visible()

    def test_guest_can_see_header_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_header_visible()

    def test_guest_can_see_get_free_views_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_get_free_views_visible()

    def test_user_can_see_popular_questions_container(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_popular_questions_container_presented()

    def test_guest_can_see_footer_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_footer_visible()

    @pytest.mark.smoke
    def test_guest_can_expand_first_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_first_question()


