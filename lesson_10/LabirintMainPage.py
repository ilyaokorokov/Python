from selenium.webdriver.common.by import By
import allure


class MainPage:

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get("https://www.labirint.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Вносим данные о куках")
    def set_cookie_policy(self):
        """
        Данный метод добавляет куки, чтобы не выводилось
        информационное сообщение.
        """
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    @allure.step("Выполняем поиск. В поле внесено - {word}")
    def search_field(self, word: str):
        """
        Данный метод принимает на вход строку, вводит её в
        поисковое поле и выполняет поиск.
        Args:
            word (str): укажите текст для выполнения поиска
        """
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(word)
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
