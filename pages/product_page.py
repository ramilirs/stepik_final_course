from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def add_book_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_basket.click()

    def should_be_correct_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BOOK), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), (
            "Message about adding is not presented")
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK).text
        book_name_original = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert basket_book_name == book_name_original, "Название книг не совпадает"

    def should_be_correct_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_COST), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.BASKET_COST), (
            "Product price is not presented")
        book_cost_basket = self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        book_cost_original = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert book_cost_basket == book_cost_original, "Цена не соответствует заявленной"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),("Message about adding is presented")

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), ("Message about adding is not dissapeared")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"