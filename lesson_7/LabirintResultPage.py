from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self._driver = driver

    def add_books(self):
        buttons = self._driver.find_elements(
            By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link"
        )

        counter = 0
        for button in buttons:
            button.click()
            counter += 1

        return counter
