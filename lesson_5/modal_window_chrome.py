from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")

button_close = ".modal-footer p"

sleep(5)
click_button_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
sleep(5)
