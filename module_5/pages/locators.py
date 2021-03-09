from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_MAIL_FIELD = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTER_MAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")



class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_MESSAGE_WITH_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_MESSAGE_WITH_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div >p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_MESSAGE_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")



