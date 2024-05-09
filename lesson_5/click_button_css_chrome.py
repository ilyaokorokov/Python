from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://uitestingplayground.com/classattr")

details = "button#details-button"
open_page = "a#proceed-link"
button_css = "button.class3.btn-primary"

click_button_details = driver.find_element(By.CSS_SELECTOR, details).click()
click_button_open_page = driver.find_element(By.CSS_SELECTOR, open_page).click()
try:
    click_button_css = driver.find_element(By.CSS_SELECTOR, button_css).click()
except:
    pass

sleep(2)
