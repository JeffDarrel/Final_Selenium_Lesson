from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BasketPage(BasePage):
    def cart_is_empty_text(self):        
        cart = self.browser.find_element(By.CSS_SELECTOR, "#content_inner p").text
        print(f"Надпись на странице корзины:{cart}")
        assert "Your basket is empty. Continue shopping" == cart, "Text is not correct"
    
    def cart_is_empty(self):
        assert self.is_not_element_present(By.CSS_SELECTOR,"#basket_formset"), \
        "Your basket is not empty"