from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADRESS = (By.ID, '#id_registration-email')
    PASSWORD = (By.ID, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//button[@name = "registration_submit"]')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_BOOK = (By.CSS_SELECTOR, '//div[@class="alertinner "]/strong')
    BOOK_NAME = (By.CSS_SELECTOR,'.product_main>h1')
    BOOK_COST = (By.XPATH, '//div/p[@class="price_color"]')
    BASKET_COST = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")