import time

import pytest

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

    def test_guest_can_see_popular_questions_container(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_popular_questions_container_presented()

    def test_guest_can_see_footer_from_faq_page(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.is_footer_visible()

    def test_guest_can_go_to_home_page_from_header_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_home_page_from_header_link()

    def test_guest_can_go_to_pricing_page_from_header_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_pricing_page_from_header_link()

    def test_guest_can_go_to_contact_us_page_from_header_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_contact_us_page_from_header_link()

    def test_guest_can_go_to_learn_page_from_header_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_learn_page_from_header_link()

    def test_guest_can_expand_collapse_first_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_first_question()
        page.collapse_first_question()

    def test_guest_can_expand_collapse_second_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_second_question()
        page.collapse_second_question()

    def test_guest_can_expand_collapse_third_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_third_question()
        page.collapse_third_question()

    def test_guest_can_expand_collapse_fourth_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_fourth_question()
        page.collapse_fourth_question()

    def test_guest_can_expand_collapse_fifth_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_fifth_question()
        page.collapse_fifth_question()

    def test_guest_can_expand_collapse_sixth_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_sixth_question()
        page.collapse_sixth_question()

    def test_guest_can_expand_collapse_seventh_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_seventh_question()
        page.collapse_seventh_question()

    def test_guest_can_expand_collapse_eighth_question(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.expand_eighth_question()
        page.collapse_eighth_question()

    def test_guest_can_go_to_home_page_from_footer_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_home_page_from_footer_link()

    def test_guest_can_go_to_pricing_page_from_footer_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_pricing_page_from_footer_link()

    def test_guest_can_go_to_contact_us_page_from_footer_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_header_link()
        page.go_to_contact_us_page_from_footer_link()

    def test_guest_can_go_to_learn_page_from_footer_link(self):
        page = FaqPage(self.driver)
        page.go_to_faq_page_from_footer_link()
        page.go_to_learn_page_from_footer_link()

