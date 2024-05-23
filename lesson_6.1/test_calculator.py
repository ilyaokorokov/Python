import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    waiter = WebDriverWait(driver, 100)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input_delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    input_delay.clear()
    input_delay.send_keys(45)

    num7 = driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[1]"
    ).click()
    num_plus = driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[4]"
    ).click()
    num8 = driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[2]"
    ).click()
    num_result = driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[15]"
    ).click()

    screen_result = driver.find_element(By.CSS_SELECTOR, "div.screen")

    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
    print(screen_result.text)
    if screen_result.text == "15":
        print("Задача выполнена")
    else:
        print("Где-то ошибка")
    driver.quit()
