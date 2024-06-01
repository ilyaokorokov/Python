from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self._driver = driver

    def get_counter(self):
        self._driver.find_element(By.CSS_SELECTOR, "a[href='/cart/']").click()
        amount = (
            self._driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']")
            .find_element(By.CSS_SELECTOR, "b")
            .text
        )
        return int(amount)

    def get_empty_result_message(self):
        txt = (
            self._driver.find_element(By.CSS_SELECTOR, "div.search-error")
            .find_element(By.CSS_SELECTOR, "h1")
            .text
        )
        return txt
