from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_be_empty_message(self):
        assert self.is_element_present(*ProductPageLocators. CART_MESSAGE_IS_EMPTY), \
            "Cart is empty message is not presented"

    def should_not_be_items_in_basket(self):
        assert not self.is_element_present(*ProductPageLocators.ITEM_IN_BASKET), \
            "Success message is presented"






