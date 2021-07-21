from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_see_product_in_basket_opened_from_product_page(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "I see some products here"

    def should_not_be_product_message(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BASKET),("Message about adding is presented")
