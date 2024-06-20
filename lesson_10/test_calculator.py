from selenium import webdriver
from CalculatorPage import Calculator
import allure


@allure.feature("Калькулятор")
@allure.title("Тест калькулятора")
@allure.description(
    "Передаем в калькулятор значения и сравниваем ОР и ФР, полученным в калькуляторе"
)
@allure.severity("Blocker")
def test_calculator():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    calculator.set_delay(45)
    calculator.get_buttons()
    total = calculator.operation(7, 8, "+", 15)
    with allure.step(
        "Проверяем, что переданный в методе результат сходится с полученным в калькуляторе"
    ):
        assert total == "15"
    calculator._driver.quit()
