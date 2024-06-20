from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver: str):
        self._driver = driver

    def get_counter(self) -> int:
        """Данный метод переводит на страницу корзины, считывает значение
        количества книг, находящихся в корзине и возвращает его.

        Returns:
            int: количество книг, находящихся в корзине
        """
        self._driver.find_element(By.CSS_SELECTOR, "a[href='/cart/']").click()
        amount = (
            self._driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']")
            .find_element(By.CSS_SELECTOR, "b")
            .text
        )
        return int(amount)

    def get_empty_result_message(self) -> str:
        """Данный метод считывает информационно сообщение, после выполнения
        поиска с отсутствующим результатом.

        Returns:
            str: текст информационного сообщения
        """
        txt = (
            self._driver.find_element(By.CSS_SELECTOR, "div.search-error")
            .find_element(By.CSS_SELECTOR, "h1")
            .text
        )
        return txt
