import time 
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):     #при обращении к этой функции будут поочередно выполняться методы описанные ниже
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REG_EMAIL_AREA)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REG_PASS_AREA1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REG_PASS_AREA2)
        input3.send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, ".btn[value='Register']").click()
        self.should_be_authorized_user() #Проверка успешности авторизации
        #Альтернативная проверка успешной регистрации:
        #assert self.is_element_present(By.CSS_SELECTOR, ".alertinner"), "Registration is not sucsess"
        #done = self.browser.find_element(By.CSS_SELECTOR, ".alertinner").text
        #print(f"Сообщение:{done}")
        
        