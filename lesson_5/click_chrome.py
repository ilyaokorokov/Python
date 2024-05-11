from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

button = "/html/body/div[2]/div/div/button"

click_button = driver.find_element(By.XPATH, button)

for new_element in range(1, 6):
    click_button.click()
    sleep(2)

button_delete = "button.added-manually"
button_list = driver.find_elements(By.CSS_SELECTOR, button_delete)

print(len(button_list))

sleep(5)
