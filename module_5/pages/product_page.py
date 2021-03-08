from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def should_show_info_in_the_cart(self):
        self.should_be_message_about_item()
        self.should_be_message_about_cost()

    def should_be_message_about_item(self):
        cart_text = self.browser.find_element(*ProductPageLocators.CART_MESSAGE_WITH_BOOK_NAME).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        whole_text = book_name + " has been added to your basket."
        assert whole_text == cart_text, "Message with book name is wrong"

    def should_be_message_about_cost(self):
        cost_text = self.browser.find_element(*ProductPageLocators.CART_MESSAGE_WITH_COST).text
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        assert book_cost in cost_text, "Message with book cost is wrong"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_disappear_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"


