from selenium import webdriver
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
