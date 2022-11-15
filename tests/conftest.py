import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


'''В этом файле conftest.py будут находиться наши Фикстуры, которые
будут помогать нашим тестам. В pytest есть зарезервированное имя для файла с фикстурами — conftest.py.'''


'''Настройки нашего браузера Chrome.'''
@pytest.fixture
def chrome_settings_options():
    options = Options()
    options.add_argument('chrome') #Опция позволит нам открывать браузер, как мы его видим
    # options.add_argument('headless') #Это если не нужен UI нашего браузера
    options.add_argument('--start-maximized') #Открывать браузер во весь экран
    return options


'''В driver записали путь к файлу и с какими опциями/настройками его будем запускать.'''
@pytest.fixture
def our_driver(chrome_settings_options):
    options = chrome_settings_options #Передали наши опции в переменную options
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\User\\OneDrive\\Рабочий стол\\chromedriver.exe',
        options=options)
    return driver


'''Выполняем это "До" и "После" запуска наших тестовых функций.
   Открываем наш сайт - "До" и "После" - закрываем все вкладки.'''
@pytest.fixture(scope='function')
def setup(our_driver):
    driver = our_driver
    base_url = 'https://www.saucedemo.com'
    driver.get(base_url)
    # Для обхода Капчи, если она есть и можно ее обойти, как Пример
    # driver.add_cookie({"name": "test", "value": "test"})
    # driver.refresh()
    yield driver #На этом месте находится наш Тест
    driver.quit()
