from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
btn_add_to_cart_locator = ".add-to-basket button[type='submit']"


def test_btn_add_to_cart_is_correct(user_language, browser):
    # Data
    buttons_text_dict = {"ru": "Добавить в корзину", "en-GB": "Add to basket", "es": "Añadir al carrito", "fr": "Ajouter au panier"}

    # Arrange
    browser.get(link)
    browser.implicitly_wait(5)

    # Act
    add_to_cart_button = browser.find_element_by_css_selector(btn_add_to_cart_locator)

    # Assert
    add_to_cart_text = add_to_cart_button.text
    assert add_to_cart_text == buttons_text_dict[user_language]
    print(add_to_cart_text, buttons_text_dict[user_language])


# def test_btn_add_to_cart_is_correct(browser):
#     # Arrange
#     browser.get(link)
#     time.sleep(3)
#     browser.find_element_by_css_selector(btn_add_to_cart)
#     add_to_cart_text = browser.find_element_by_css_selector(btn_add_to_cart).text
#
#     # Act
#     ru_language = browser.find_element_by_css_selector("option[value='ru']")
#     es_language = browser.find_element_by_css_selector("option[value='es']")
#     fr_language = browser.find_element_by_css_selector("option[value='fr']")
#     en_gb_language = browser.find_element_by_css_selector("option[value='en-gb']")
#
#     # Assert
#     if ru_language.is_selected():
#         assert add_to_cart_text == "Добавить в корзину", "Текст на кнопке добавления товара в корзину не верный"
#         print(add_to_cart_text)
#     elif es_language.is_selected():
#         assert add_to_cart_text == "Añadir al carrito", "Текст на кнопке добавления товара в корзину не верный"
#         print(add_to_cart_text)
#     elif fr_language.is_selected():
#         assert add_to_cart_text == "Ajouter au panier", "Текст на кнопке добавления товара в корзину не верный"
#         print(add_to_cart_text)
#     elif en_gb_language.is_selected():
#         assert add_to_cart_text == "Add to basket", "Текст на кнопке добавления товара в корзину не верный"
#         print(add_to_cart_text)
