import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["0","1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}" #f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" #"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   
    page.open()                      
    page.promo_buy()
