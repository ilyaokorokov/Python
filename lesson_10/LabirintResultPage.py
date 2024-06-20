from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver: str):
        self._driver = driver

    def add_books(self) -> int:
        """
        Данный метод добавляет книгу в корзину и считает
        количество выполненных нажатий на кнопку "В корзину".

        Returns:
            int: количество нажатий (добавлений) в корзину
        """
        buttons = self._driver.find_elements(
            By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link"
        )

        counter = 0
        for button in buttons:
            button.click()
            counter += 1

        return counter
