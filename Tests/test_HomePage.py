import pytest

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):
    def test_signup_button_is_visible(self):
        page = BasePage(self.driver)
        page.is_signup_button_exist()

    def test_home_page_title(self):
        page = HomePage(self.driver)
        page.check_home_page_title()

    def test_guest_can_see_header_logo_from_home_page(self):
        page = BasePage(self.driver)
        page.is_header_logo_visible()

    def test_guest_can_see_header_from_home_page(self):
        page = BasePage(self.driver)
        page.is_header_visible()

    def test_guest_can_see_how_it_works_button(self):
        page = HomePage(self.driver)
        page.is_how_it_works_button_presented()

    def test_guest_can_see_make_an_order_button(self):
        page = HomePage(self.driver)
        page.is_make_an_order_button_presented()

    @pytest.mark.smoke
    def test_guest_can_see_boost_your_profile_section(self):
        page = HomePage(self.driver)
        page.is_boost_your_profile_container_presented()

    def test_guest_can_see_footer_from_home_page(self):
        page = BasePage(self.driver)
        page.is_footer_visible()

    def test_guest_can_see_get_free_views_from_home_page(self):
        page = BasePage(self.driver)
        page.is_get_free_views_visible()

    def test_guest_can_see_what_do_we_offer_section(self):
        page = HomePage(self.driver)
        page.is_what_do_we_offer_container_presented()

    def test_guest_can_see_what_we_have_already_done_section(self):
        page = HomePage(self.driver)
        page.is_what_we_have_already_done_container_presented()

    def test_guest_can_see_promotion_formats_section(self):
        page = HomePage(self.driver)
        page.is_promotion_formats_container_presented()

    def test_guest_can_see_our_clients_trust_us_section(self):
        page = HomePage(self.driver)
        page.is_our_clients_trust_us_container_presented()

    def test_guest_can_see_any_questions_section(self):
        page = HomePage(self.driver)
        page.is_any_questions_container_presented()

    def test_user_can_go_to_pricing_page_from_header_link(self):
        page = BasePage(self.driver)
        page.go_to_pricing_page_from_header_link()

    def test_user_can_go_to_faq_page_from_header_link(self):
        page = BasePage(self.driver)
        page.go_to_faq_page_from_header_link()

    def test_user_can_go_to_contact_us_page_from_header_link(self):
        page = BasePage(self.driver)
        page.go_to_contact_us_page_from_header_link()

    def test_user_can_go_to_pricing_page_from_footer_link(self):
        page = BasePage(self.driver)
        page.go_to_pricing_page_from_footer_link()

    def test_user_can_go_to_faq_page_from_footer_link(self):
        page = BasePage(self.driver)
        page.go_to_faq_page_from_footer_link()

    def test_user_can_go_to_contact_us_page_from_footer_link(self):
        page = BasePage(self.driver)
        page.go_to_contact_us_page_from_footer_link()

    def test_user_can_go_to_pricing_page_from_boost_your_profile_section(self):
        page = HomePage(self.driver)
        page.go_to_pricing_page_from_boost_your_profile_section()

    def test_user_can_go_to_pricing_page_from_what_do_we_offer_section(self):
        page = HomePage(self.driver)
        page.go_to_pricing_page_from_what_do_we_offer_section()

    def test_user_can_go_to_pricing_page_from_promotion_formats_section(self):
        page = HomePage(self.driver)
        page.go_to_pricing_page_from_promotion_formats_section()

    def test_user_can_go_to_faq_page_from_any_questions_section(self):
        page = HomePage(self.driver)
        page.go_to_faq_page_from_any_questions_section()

    def test_user_can_go_to_contact_us_page_from_any_questions_section(self):
        page = HomePage(self.driver)
        page.go_to_contact_us_page_from_any_questions_section()


