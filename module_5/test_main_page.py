from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # проверяем страницу логина

    def test_guest_should_see_login_link_on_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)  # передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_basket()  # переходим на страницу корзины
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_message()  # проверяем сообщение что корзина пуста
        basket_page.should_not_be_items_in_basket()  # проверяем что нет товаров в корзине

#pytest -v --tb=line --language=en-GB module_5\test_main_page.py

