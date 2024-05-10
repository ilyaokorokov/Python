from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")

button_close = ".modal-footer p"

sleep(5)
click_button_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
sleep(5)
driver.quit()
