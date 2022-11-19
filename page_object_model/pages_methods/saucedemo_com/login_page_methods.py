from page_object_model.pages_locators.locators_saucedemo_com import *
from selenium.webdriver import Keys
from page_object_model.base import Base_methods


class Login_page_methods:


    """Авторизация Пользователя на saucedemo.com"""
    @staticmethod
    def authorization_in_account(our_driver, setup, user : dict):
        driver = setup
        Base_methods.get_element(our_driver, Login_page_locators.USERNAME_FIELD).send_keys(user['user_name'])
        Base_methods.get_element(our_driver, Login_page_locators.PASSWORD_FIELD).send_keys(user['password'], Keys.ENTER)
        products_text = Base_methods.get_element(our_driver, Main_page_locators.SEE_PRODUCTS_TEXT).text
        assert products_text == 'PRODUCTS', f'Текст {products_text} отличается от текста "PRODUCTS"'
        account_url = driver.current_url
        assert 'inventory' in account_url, f'Не верный {account_url} url'
