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

    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(
        "Ленина, 55-3"
    )
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(
        "test@skypro.com"
    )
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(
        "+7985899998787"
    )
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    driver.find_element(
        By.CSS_SELECTOR, 'button.btn-outline-primary[type="submit"]'
    ).click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    address = driver.find_element(By.CSS_SELECTOR, "#address")
    email = driver.find_element(By.CSS_SELECTOR, "#e-mail")
    phone_number = driver.find_element(By.CSS_SELECTOR, "#phone")
    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    city = driver.find_element(By.CSS_SELECTOR, "#city")
    country = driver.find_element(By.CSS_SELECTOR, "#country")
    job_position = driver.find_element(By.CSS_SELECTOR, "#job-position")
    company = driver.find_element(By.CSS_SELECTOR, "#company")

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

    driver.quit()
