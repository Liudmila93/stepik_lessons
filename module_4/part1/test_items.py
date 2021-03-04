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

