from page_object_model.constants import *
from page_object_model.base import Base_methods
from page_object_model.pages_locators.locators_saucedemo_com import *
from page_object_model.pages_methods.saucedemo_com.login_page_methods import Login_page_methods
import pytest
import allure


@allure.feature('saucedemo.com')
class Test_check_social_networks:


    """Проверка ссылок социальных сетей"""
    @allure.title('Проверка социальных сетей')
    @pytest.mark.ui_saucedemo
    def test_check_social_networks(self, our_driver, setup):
        driver = our_driver
        Login_page_methods.authorization_in_account(our_driver, setup, User_constants_saucedemo_com.STANDARD_USER)
        social_networks_and_locators = {
        'twitter': Main_page_locators.TWITTER,
        'facebook': Main_page_locators.FACEBOOK,
        'linkedin': Main_page_locators.LINKEDIN}
        index_window_handles = 1
        for social_networks, locators in social_networks_and_locators.items():
            Base_methods.get_element(our_driver, locators).click()
            window_social_networks = driver.window_handles[index_window_handles]
            driver.switch_to.window(window_social_networks)
            assert social_networks in driver.current_url, f'{social_networks} отсутствует в нашем url {driver.current_url}'
            main_window = driver.window_handles[0]
            driver.switch_to.window(main_window)
            index_window_handles += 1
