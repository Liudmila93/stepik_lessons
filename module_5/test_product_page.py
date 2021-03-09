from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time

#
# class TestProductPage:
#     @pytest.mark.parametrize('promo_offer',
#                               ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
#                                pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
#                                "offer9"])
#     def test_guest_can_add_product_to_basket(self, browser, promo_offer):
#         link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
#         page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
#         page.open()  # открываем страницу
#         page.add_item_to_basket()  # выполняем метод страницы - нажимаем на кнопку добавления в корзину
#         page.solve_quiz_and_get_code()
#         page.should_show_info_in_the_cart()  # проверяем страницу логина
#
#     @pytest.mark.xfail(reason="user will see success message in this test")
#     def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()  # открываем страницу
#         page.add_item_to_basket()  # нажимаем на кнопку добавления в корзину
#         page.solve_quiz_and_get_code()
#         page.should_not_be_success_message()  # проверяем страницу логина
#
#     def test_guest_cant_see_success_message(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()  # открываем страницу
#         page.should_not_be_success_message()  # проверяем страницу логина
#
#     @pytest.mark.xfail(reason="success message cant dissapear")
#     def test_message_disappeared_after_adding_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()  # открываем страницу
#         page.add_item_to_basket()  # нажимаем на кнопку добавления в корзину
#         page.solve_quiz_and_get_code()
#         page.should_disappear_success_message()  # проверяем страницу логина
#
#     def test_guest_should_see_login_link_on_product_page(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#         page = ProductPage(browser, link)
#         page.open()
#         page.should_be_login_link()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()
#         page.should_be_login_link()
#
#     def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()
#         page.go_to_basket()
#         basket_page = BasketPage(browser, browser.current_url)
#         basket_page.should_be_empty_message()  # проверяем сообщение что корзина пуста
#         basket_page.should_not_be_items_in_basket()  # проверяем что нет товаров в корзине


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = ProductPage(browser, link)
        page.open()
        login_new_user = LoginPage(browser, link)
        login_new_user.register_new_user(email=str(time.time()) + "@fakemail.org", password="Qwerty123!!")
        check = BasePage(browser, link)
        check.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # проверяем страницу логина

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()  # открываем страницу
        page.add_item_to_basket()  # выполняем метод страницы - нажимаем на кнопку добавления в корзину
        page.should_show_info_in_the_cart()  # проверяем страницу логина

# pytest -v --tb=line --language=en-GB module_5\test_main_page.py
