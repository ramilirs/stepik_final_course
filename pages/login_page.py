from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_adress = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS)
        email_adress.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        register_button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Can't find word login in url"# реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" # реализуйте проверку, что есть форма регистрации на странице