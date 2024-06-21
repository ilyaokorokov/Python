from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Устанавливаем значение задержки - {delay}")
    def set_delay(self, delay: int):
        """
        Данный метод получает на вход значение, которое необходимо
        установить в качестве задержки перед получением результата.

        Вносит полученное значение в соответствующее поле.

        Args:
            delay (int): величина задержки
        """
        self._delay = delay
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    @allure.step("Разбираем кнопки калькулятора по классам и сохраняем в переменные")
    def get_buttons(self):
        """
        Данный метод собирает информацию по всем кнопках калькулятора
        и сохраняет в переменные. Переменные содержат список кнопок определенного класса.
        Числовые кнопки, кнопки-операторы, кнопка равно, кнопка очистки, поле результата.
        """
        self.buttons = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn-outline-primary"
        )
        self.operators = self._driver.find_elements(By.CSS_SELECTOR, ".operator")
        self.equal = self._driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-warning"
        )
        self.clear = self._driver.find_element(
            By.CSS_SELECTOR, ".clear.btn.btn-outline-danger"
        )
        self.screen_result = self._driver.find_element(By.CSS_SELECTOR, "div.screen")

    @allure.step(
        "Считываем переданные в методе значения, нажимаем соответствующие кнопки в калькуляторе, получаем результат и возвращаем его. Первое число - {num1}, второе - {num2}, оператор - {operator}, результат - {total}."
    )
    def operation(self, num1: int, num2: int, operator: str, total: int) -> str:
        """Данный метод получает на вход 2 числа, оператор и результат
        операции. Производит расчёт в калькуляторе, дожидается
        появление значения в окне результата и возвращает его.

        Args:
            num1 (int): первое целое число
            num2 (int): второе целое число
            operator (str): операторы +, -, *, /
            total (int): результат операции первого и второго числа

        Returns:
            str: фактический результат операции считанный из поля
        """
        num1_str = str(num1)
        num2_str = str(num2)

        num1_button = None
        num2_button = None
        operator_button = None

        with allure.step("Проверяем полученные значения и нажимаем кнопки"):
            for button in self.buttons:
                if button.text == num1_str:
                    num1_button = button
                elif button.text == num2_str:
                    num2_button = button

            for button in self.operators:
                if button.text == operator:
                    operator_button = button

            if num1_button and num2_button and operator_button:
                num1_button.click()
                operator_button.click()
                num2_button.click()
                self.equal.click()

        with allure.step("Ожидаем получение результата и возвращаем его"):
            WebDriverWait(self._driver, 100).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "div.screen"), str(total)
                )
            )
            return self.screen_result.text
