from page_object_model.constants import *
from page_object_model.base import Base_methods
import pytest


class Test_performance_glitch_authorization:


    """Авторизация с пользователем, у которого медленный интернет на saucedemo.com"""
    @pytest.mark.ui_saucedemo
    def test_performance_glitch_authorization(self, our_driver, setup):
        Base_methods.authorization_in_account(our_driver, setup, User_constants.PERFOMANCE_GLITCH_USER)
