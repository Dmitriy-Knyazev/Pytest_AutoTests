from page_object_model.constants import *
from page_object_model.pages_methods.saucedemo_com.login_page_methods import Login_page_methods
from page_object_model.base import Base_methods
from page_object_model.pages_locators.locators_saucedemo_com import Main_page_locators
import pytest
import allure


"""Тест с ошибкой"""
@allure.feature('saucedemo.com')
class Test_with_error:


    @allure.title('Тест с ошибкой')
    @pytest.mark.ui_saucedemo
    def test_with_error(self, our_driver, setup):
        Login_page_methods.authorization_in_account(our_driver, setup, User_constants_saucedemo_com.STANDARD_USER)
        products_text = Base_methods.get_element(our_driver, Main_page_locators.SEE_PRODUCTS_TEXT).text
        assert products_text == 'ERROR', f'Текст {products_text} отличается от текста "ERROR"'
