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
        time.sleep(3)

    def test_user_can_choose_likes(self):
        page = PricingPage(self.driver)
        page.go_to_pricing_page_from_header_link()
        page.choose_likes()
        time.sleep(3)

