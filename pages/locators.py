from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_NAME_CART = (By.CSS_SELECTOR, ".alert:nth-last-child(3)  strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(2)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #некорректный селектор для проверок
    CART_HEADER_LINK = (By.CSS_SELECTOR, ".btn-group .btn")