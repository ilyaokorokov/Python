from selenium import webdriver
from LabirintMainPage import MainPage
from LabirintResultPage import ResultPage
from LabirintCartPage import CartPage
import allure
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    return main_page

@allure.feature("Лабиринт")
class TestLabirint:

    @pytest.mark.usefixtures("driver", "main_page")
    @allure.title("Тест счётчика товаров в корзине")
    @allure.description(
        "Ищем необходимую книгу, добавляем в корзину товары и проверяем количество товаров в корзине со значением счетчика товаров"
    )
    @allure.severity("Normal")
    def test_labirint_cart_counter(self, main_page, driver):
        main_page.search_field("Python")
        with allure.step(
            "На странице результата поиска добавляем все книги в корзину и считаем сколько было добавлено"
        ):
            result_page = ResultPage(driver)
            expected_result = result_page.add_books()
        with allure.step(
            "Переходим в корзину и получаем значение количества товаров в корзине"
        ):
            cart_page = CartPage(driver)
            actual_result = cart_page.get_counter()
        with allure.step(
            "Проверяем, что отображаемое значение товаров в корзине соответствует количеству добавленных книг"
        ):
            assert actual_result == expected_result

    @pytest.mark.usefixtures("driver", "main_page")
    @allure.title(
        "Информационное сообщение при отсутствии совпадений результата поиска"
    )
    @allure.description(
        "Выполняем поиск по несуществующему названию книги и сверяем полученное информационное сообщение с шаблоном"
    )
    @allure.severity("Minor")
    def test_labirint_empty_search(self, main_page, driver):
        main_page.search_field("no book search term")
        with allure.step(
            "Переходим на страницу результата поиска и считываем информационное сообщение"
        ):
            cart_page = CartPage(driver)
            message = cart_page.get_empty_result_message()
        with allure.step(
            "Проверяем, что информационное сообщение соответствует шаблону"
        ):
            assert message == "Мы ничего не нашли по вашему запросу! Что делать?"