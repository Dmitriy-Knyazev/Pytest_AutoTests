import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests


class Base_methods:


    """Поиск Элементов"""
    @staticmethod
    def get_element(our_driver, locator):
        driver = our_driver
        wait = WebDriverWait(driver, 5, 0.3)
        web_element = wait.until(ec.visibility_of_element_located(locator))
        return web_element


    """Проверка Статус кода"""
    @staticmethod
    def check_status_code(response, expected_code):
        status_code = response.status_code
        assert status_code == expected_code, f'Статус код ответа {status_code} не равен ожидаемому коду {expected_code}'


    """POST ЗАПРОС"""
    @staticmethod
    def api_post(url, body: dict):
        response = requests.post(url, body)
        Base_methods.check_status_code(response, 200)
        return response


    """GET ЗАПРОС"""
    @staticmethod
    def api_get(url):
        response = requests.get(url)
        Base_methods.check_status_code(response, 200)
        return response


    '''Метод для проверки в API наличия обязательных параметров в ответе запроса'''
    @staticmethod
    def check_json_params(response, expected_value):
        json_data = json.loads(response.text)
        assert list(json_data) == expected_value


    '''Метод для проверки в API, наличие слов в значениях параметров'''
    @staticmethod
    def check_json_words_in_value(response, parameter, word_or_words):
        check_info = response.json()
        check_value = check_info.get(parameter)
        assert word_or_words in check_value, f'Слово {word_or_words} отсутствует в {check_value}'


    '''Метод API, проверка значения параметра'''
    @staticmethod
    def check_value_in_parameter(response, parameter, expected_value):
        check_info = response.json()
        check_value = check_info.get(parameter)
        assert expected_value == check_value, f'Ожидаемое значение {expected_value} не равно явному {check_value}'


    """Разлогиниться"""
    @staticmethod
    def logout(our_driver):
        driver = our_driver
