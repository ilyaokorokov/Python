from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

username = "input[name='username']"
password = "input[name='password']"
button_login = "button.radius"

input_username = driver.find_element(By.CSS_SELECTOR, username).send_keys("tomsmith")
sleep(3)
input_password = driver.find_element(By.CSS_SELECTOR, password).send_keys(
    "SuperSecretPassword!"
)
sleep(3)
press_button = driver.find_element(By.CSS_SELECTOR, button_login).click()
sleep(3)
