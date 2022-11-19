import pytest
import allure


"""Тестирование SQL Тренажера https://sql-academy.org/ru/trainer"""
@allure.feature('sql-academy.org')
class Test_sql_trainer:


    @pytest.mark.sql
    def test_sql_trainer(self):
        pass
