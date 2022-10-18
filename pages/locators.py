from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_AREA = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS_AREA1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_AREA2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, ".btn[value='Register']")
    
class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_NAME_CART = (By.CSS_SELECTOR, ".alert:nth-last-child(3)  strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(2)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #некорректный селектор для negative тестов
    CART_HEADER_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_TXT = (By.CSS_SELECTOR, "#content_inner p")