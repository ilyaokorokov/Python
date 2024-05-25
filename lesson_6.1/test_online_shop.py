from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")

button = driver.find_element(By.CSS_SELECTOR, "#login-button")
button.click()

backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
backpack.click()

tshirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
tshirt.click()

onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
onesie.click()

shop_cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
shop_cart.click()

checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout_button.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Илья")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Окороков")

postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys(350024)

continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
continue_button.click()


total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

if total == "Total: $58.29":
    print("Задача выполнена")
else:
    print("Где-то ошибка")

driver.quit()
