from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_delay(self, delay: str):
        self._delay = delay
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    def get_buttons(self):
        self.buttons = self._driver.find_elements(By.CSS_SELECTOR, ".btn.btn-outline-primary")
        self.operators = self._driver.find_elements(By.CSS_SELECTOR, ".operator")
        self.equal = self._driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-warning"
        )
        self.clear = self._driver.find_element(
            By.CSS_SELECTOR, ".clear.btn.btn-outline-danger"
        )
        self.screen_result = self._driver.find_element(By.CSS_SELECTOR, "div.screen")

    def operation(self, num1: int, num2: int, operator: str, total: int):
        num1_str = str(num1)
        num2_str = str(num2)

        num1_button = None
        num2_button = None
        operator_button = None

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

        WebDriverWait(self._driver, 100).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), str(total)
            )
        )
        print(self.screen_result.text)
        if self.screen_result.text == str(total):
            print("Задача выполнена, ОР совпадает с ФР")
        else:
            print("Где-то ошибка")
