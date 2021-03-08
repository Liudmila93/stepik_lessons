from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                              ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                               "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_basket_page()  # выполняем метод страницы - нажимаем на кнопку добавления в корзину
        page.solve_quiz_and_get_code()
        page.should_show_info_in_the_cart()  # проверяем страницу логина



#pytest -v --tb=line --language=en-GB module_5\test_main_page.py

