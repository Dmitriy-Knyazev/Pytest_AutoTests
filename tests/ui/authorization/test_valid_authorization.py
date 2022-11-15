from page_object_model.constants import *
from page_object_model.base import Base_methods


"""Валидная Авторизация на saucedemo.com"""
class Test_valid_authorization:


    """Валидная Авторизация на saucedemo.com"""
    def test_valid_authorization(self, our_driver, setup):
        Base_methods.authorization_in_account(our_driver, setup, User_constants.STANDARD_USER)
