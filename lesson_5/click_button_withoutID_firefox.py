from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://uitestingplayground.com/dynamicid")

button_dynamic = "button.btn.btn-primary"

click_button_dynamic = driver.find_element(By.CSS_SELECTOR, button_dynamic).click()
sleep(5)
driver.quit()
