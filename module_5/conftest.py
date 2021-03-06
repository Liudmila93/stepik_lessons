"""Файл conftest.py имеет следующее содержание:

conftest.py содержит обработчик опции language
conftest.py содержит фикстуру browser
В фикстуре browser создается и возвращается объект браузера с языковыми настройками, соответствующими переданной опции language
В фикстуре browser реализовано закрытие браузера после прохождения теста"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")


@pytest.fixture(scope="function")
def user_language(request):
    user_language = request.config.getoption("language")
    if user_language in ["ru", "en-GB", "fr", "es"]:
        print("User language is", user_language)
        return user_language
    else:
        raise pytest.UsageError("--language should be ru or en-GB or es or fr")

@pytest.fixture(scope="function")
def browser(user_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()




#pytest -s -v --language=es module_4\part1\test_items.py
