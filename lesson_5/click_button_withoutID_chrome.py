from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://uitestingplayground.com/dynamicid")

details = "button#details-button"
open_page = "a#proceed-link"
button_dynamic = "button.btn.btn-primary"

click_button_details = driver.find_element(By.CSS_SELECTOR, details).click()
click_button_open_page = driver.find_element(By.CSS_SELECTOR, open_page).click()
click_button_dynamic = driver.find_element(By.CSS_SELECTOR, button_dynamic).click()
sleep(5)
