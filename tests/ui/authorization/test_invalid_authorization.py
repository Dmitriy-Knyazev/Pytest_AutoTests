from page_object_model.constants import *
from page_object_model.base import Base_methods
from page_object_model.pages_locators.locators_saucedemo_com import *
from selenium.webdriver import Keys
import pytest


"""Невалидная Авторизация на saucedemo.com"""
class Test_invalid_authorization:


    """Невалидная Авторизация на saucedemo.com"""
    @pytest.mark.ui_saucedemo
    def test_invalid_authorization(self, our_driver, setup):
        driver = setup
        Base_methods.get_element(our_driver, Login_page_locators.USERNAME_FIELD).\
            send_keys(User_constants.LOCKED_USER['user_name'])
        Base_methods.get_element(our_driver, Login_page_locators.PASSWORD_FIELD).\
            send_keys(User_constants.LOCKED_USER['password'], Keys.ENTER)
        error_text = Base_methods.get_element(our_driver, Login_page_locators.ERROR_TEXT).text
        assert error_text == 'Epic sadface: Sorry, this user has been locked out.', \
            f'Пользователь {User_constants.LOCKED_USER} не заблокирован?'
        login_url = driver.current_url
        assert 'https://www.saucedemo.com/' == login_url, f'Не верный {login_url} url'
