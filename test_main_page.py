from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()

@pytest.mark.new

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.should_not_see_product_in_basket_opened_from_product_page()
    page.should_not_be_product_message()

