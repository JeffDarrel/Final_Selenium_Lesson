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
    
@pytest.mark.skip #красный тест по заданию из 6 шага
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   
    page.open()
    page.adding_to_cart()
    page.should_not_be_success_message()
  
def test_guest_cant_see_success_message(browser): 
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.skip #красный тест по заданию из 6 шага
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   
    page.open()
    page.adding_to_cart()
    page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()