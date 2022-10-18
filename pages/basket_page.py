from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BasketPage(BasePage):
    def cart_is_empty_text(self):        
        cart = self.browser.find_element(*BasePageLocators.BASKET_TXT).text
        print(f"Надпись на странице корзины:{cart}")
        assert "Your basket is empty. Continue shopping" == cart, "Text is not correct"
    
    def cart_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_FORMSET), \
        "Your basket is not empty"