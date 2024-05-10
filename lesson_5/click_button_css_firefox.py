from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://uitestingplayground.com/classattr")

button_css = "button.btn-primary"

try:
    click_button_css = driver.find_element(By.CSS_SELECTOR, button_css).click()
except:
    pass

sleep(2)
driver.quit()
