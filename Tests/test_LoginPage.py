import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_create_account_with_email(self, email='user1@mail.ru', password=TestData.PASSWORD):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_sign_up_tab()
        page.set_email(email=email)
        page.set_password(password=password)
        page.click_create_my_account_button()

    def test_guest_cant_register_without_filling_email(self, email='', password=TestData.PASSWORD):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_sign_up_tab()
        page.set_email(email=email)
        page.set_password(password=password)
        page.click_create_account_disabled_button()
        page.is_required_field()
        time.sleep(5)

    def test_guest_cant_register_without_filling_password(self, email='user123@mail.ru', password=''):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_sign_up_tab()
        page.set_email(email=email)
        page.set_password(password=password)
        page.click_create_account_disabled_button()
        page.is_required_field()
        time.sleep(5)

    def test_login(self, email='user@mail.ru', password=TestData.PASSWORD):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_login_tab()
        page.set_email(email=email)
        page.set_password(password=password)
        page.click_login_button()

    def test_user_can_open_login_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()

    def test_user_can_close_logit_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_close_login_page()

    def test_user_can_open_forgot_password_form(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_forgot_password_button()

