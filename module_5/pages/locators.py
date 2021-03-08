from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_MESSAGE_WITH_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_MESSAGE_WITH_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div >p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_MESSAGE_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")



