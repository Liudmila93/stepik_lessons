
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_cart_is_correct(browser):
    browser.get(link)
    time.sleep(3)
    btn_add_to_cart = browser.find_element_by_css_selector(".add-to-basket button[type='submit']")
    add_to_cart = btn_add_to_cart.text
    ru_language = browser.find_element_by_css_selector("option[value='ru']")
    es_language = browser.find_element_by_css_selector("option[value='es']")
    fr_language = browser.find_element_by_css_selector("option[value='fr']")
    en_gb_language = browser.find_element_by_css_selector("option[value='en-gb']")
    if ru_language.is_selected():
        assert add_to_cart == "Добавить в корзину", "Текст на кнопке добавления товара в корзину не верный"
        print(add_to_cart)
    elif es_language.is_selected():
        assert add_to_cart == "Añadir al carrito", "Текст на кнопке добавления товара в корзину не верный"
        print(add_to_cart)
    elif fr_language.is_selected():
        assert add_to_cart == "Ajouter au panier", "Текст на кнопке добавления товара в корзину не верный"
        print(add_to_cart)
    elif en_gb_language.is_selected():
        assert add_to_cart == "Add to basket", "Текст на кнопке добавления товара в корзину не верный"
        print(add_to_cart)


