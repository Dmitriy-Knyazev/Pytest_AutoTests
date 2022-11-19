from page_object_model.constants import *
from page_object_model.pages_methods.saucedemo_com.login_page_methods import Login_page_methods
import pytest


"""Валидная Авторизация на saucedemo.com"""
class Test_valid_authorization:


    """Валидная Авторизация на saucedemo.com"""
    @pytest.mark.ui_saucedemo
    def test_valid_authorization(self, our_driver, setup):
        Login_page_methods.authorization_in_account(our_driver, setup, User_constants_saucedemo_com.STANDARD_USER)
