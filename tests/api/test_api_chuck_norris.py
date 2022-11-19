import pytest
from page_object_model.base import Base_methods


"""Тестирование api Chuck Norris https://api.chucknorris.io"""
@pytest.mark.api_chuck_norris
class Test_api_chuck_norris:

    categories = ["animal", "career", "celebrity", "dev", "explicit",
                  "fashion", "food", "history", "money", "movie", "music",
                  "political", "religion", "science", "sport", "travel"]

    expected_value = ['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value']


    """Проверка случайной шутки"""
    def test_api_random_jokes(self):
        random_jokes = 'https://api.chucknorris.io/jokes/random'
        response = Base_methods.api_get(random_jokes)
        Base_methods.check_json_params(response, Test_api_chuck_norris.expected_value)
        Base_methods.check_json_words_in_value(response, 'value', 'Chuck Norris')


    """Проверка списка категорий"""
    def test_api_check_list_categories(self):
        categories_url = 'https://api.chucknorris.io/jokes/categories'
        response = Base_methods.api_get(categories_url)
        Base_methods.check_json_params(response, Test_api_chuck_norris.categories)


    """Проверка GET запросов со всеми категориями"""
    @pytest.mark.xfail(reason='Иногда Тест падает, не всегда в ответе есть имя "Chuck Norris"')
    def test_api_check_value_categories(self):
        for our_categories in Test_api_chuck_norris.categories:
            sub_url = 'https://api.chucknorris.io/jokes/random?category='
            main_url = sub_url + our_categories
            response = Base_methods.api_get(main_url)
            Base_methods.check_json_params(response, Test_api_chuck_norris.expected_value)
            Base_methods.check_json_words_in_value(response, 'value', 'Chuck Norris')


    """Проверка наличие числа ответов со словом 'bitch'"""
    def test_api_check_value_with_word(self):
        sub_url = 'https://api.chucknorris.io/jokes/search?query='
        our_word = 'bitch'
        main_url = sub_url + our_word
        response = Base_methods.api_get(main_url)
        Base_methods.check_value_in_parameter(response, 'total', 35)


    """Один Тест с маркером parametrize"""
    @pytest.mark.parametrize('categories', [
        "animal", "career", "celebrity", "dev", "explicit",
        "fashion", "food", "history", "money", "movie", "music",
        "political", "religion", "science", "sport", "travel"])
    def test_one_test_with_parametrize(self, categories):
        category_url = f'https://api.chucknorris.io/jokes/random?category={categories}'
        response = Base_methods.api_get(category_url)
        Base_methods.check_json_params(response, Test_api_chuck_norris.expected_value)
        Base_methods.check_json_words_in_value(response, 'value', 'Chuck Norris')
