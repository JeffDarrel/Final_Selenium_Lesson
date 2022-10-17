from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

     
class ProductPage(BasePage):
    def promo_buy(self):
        self.adding_to_cart()
        self.promo_quiz_code()
        self.cart_matching()
        self.book_comparison()

    def adding_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        link.click()
    
    def promo_quiz_code(self):
        self.solve_quiz_and_get_code()
                        
    def cart_matching(self):
        price1 = self.browser.find_element(*ProductPageLocators.MAIN_PRICE).text
        print(f"Стоимость в карточке товара:{price1}")
        price2 = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        print(f"Стоимость в корзине:{price2}")
        assert price1 == price2, "The amount in the cart is not equal to the value of the product"
    
    def book_comparison(self):
        book1 = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(f"Название книги в карточке товара:{book1}")
        book2 = self.browser.find_element(*ProductPageLocators.BOOK_NAME_CART).text
        print(f"Название книги в корзине:{book2}")
        assert book1 == book2, "The name of the book in the cart does not match the name in the product card"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
        
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message disappears, but should not be"