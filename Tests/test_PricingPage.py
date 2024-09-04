import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.PricingPage import PricingPage
from Tests.test_base import BaseTest


class TestPricingPage(BaseTest):

    def test_pricing_page_title(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.check_pricing_page_title()
        time.sleep(1)

    def test_user_can_choose_likes(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_likes()
        time.sleep(1)

    def test_user_can_choose_views(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_views()
        time.sleep(1)

    def test_user_can_choose_followers(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_followers()
        time.sleep(1)

    def test_user_can_choose_comments(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_comments()
        time.sleep(1)

    def test_user_can_choose_reposts(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_reposts()
        time.sleep(1)

    def test_user_can_decrease_number_of_action(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_views()
        page.increase_number(5)

    def test_user_can_enter_number_manually(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.enter_number_manually(10)

