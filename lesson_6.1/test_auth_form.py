import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_auth_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number.send_keys("+7985899998787")

    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_code.clear()

    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, 'button.btn-outline-primary[type="submit"]'
    )
    submit_button.click()

    success_class = "alert-success"
    danger_class = "alert-danger"

    fields = [
        first_name,
        last_name,
        address,
        email,
        phone_number,
        city,
        country,
        job_position,
        company,
    ]

    for element in fields:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )
        result = element.get_attribute("class")
        print(result)
        assert success_class in result

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger"))
    )
    danger_element = zip_code.get_attribute("class")
    assert danger_class in danger_element

    print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)

    driver.quit()
