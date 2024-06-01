import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from AuthPage import Auth
from CalculatorPage import Calculator
from OnlineShopPage import OnlineShop
from LabirintMainPage import MainPage
from LabirintResultPage import ResultPage
from LabirintCartPage import CartPage


def test_labirint_cart_counter():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search_field("Python")
    result_page = ResultPage(driver)
    expected_result = result_page.add_books()
    cart_page = CartPage(driver)
    actual_result = cart_page.get_counter()
    assert actual_result == expected_result
    driver.quit()


def test_labirint_empty_search():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search_field("no book search term")
    cart_page = CartPage(driver)
    message = cart_page.get_empty_result_message()
    assert message == "Мы ничего не нашли по вашему запросу! Что делать?"
    driver.quit()


def test_auth_form():
    driver = webdriver.Chrome()
    auth_page = Auth(driver)
    auth_page.submit_form(
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "",
        "Москва",
        "Россия",
        "test@skypro.com",
        "+7985899998787",
        "QA",
        "SkyPro",
    )
    auth_page.response_form()
    auth_page.get_result()
    auth_page._driver.quit()


def test_calculator():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    calculator.set_delay("45")
    calculator.get_buttons()
    calculator.operation(7, 8, "+", 15)
    calculator._driver.quit()


def test_online_shop():
    driver = webdriver.Chrome()
    online_shop = OnlineShop(driver)
    online_shop.user_auth("standard_user", "secret_sauce")
    online_shop.get_info_and_buttons()
    online_shop.add_items_to_cart(
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
    )
    online_shop.place_order("Илья", "Окороков", "350024")
    online_shop.get_result_price()
    online_shop._driver.quit()
