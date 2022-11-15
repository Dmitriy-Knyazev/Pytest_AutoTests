from selenium.webdriver.common.by import By


"""Локаторы страницы Логина saucedemo.com"""
class Login_page_locators:

    USERNAME_FIELD = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    ERROR_TEXT = (By.XPATH, '//*[text()="Epic sadface: Sorry, this user has been locked out."]')


"""Локаторы Главной страницы saucedemo.com"""
class Main_page_locators:

    SEE_PRODUCTS_TEXT = (By.XPATH, '//*[text()="Products"]')
