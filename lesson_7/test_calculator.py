from selenium import webdriver
from CalculatorPage import Calculator


def test_calculator():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    calculator.set_delay("45")
    calculator.get_buttons()
    total = calculator.operation(7, 8, "+", 15)
    assert total == "15"
    calculator._driver.quit()
