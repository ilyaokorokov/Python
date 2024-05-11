from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

yandex_browser_path = (
    "C:\\Users\\Илья\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
)

driver_path = "C:\\Users\\Илья\\Desktop\\chromedriver-win64-yabrowser\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.binary_location = yandex_browser_path

# Запуск сервиса ChromeDriver
service = ChromeService(driver_path)

# Запуск драйвера Chrome с указанием сервиса и опций
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

button = "/html/body/div[2]/div/div/button"

click_button = driver.find_element(By.CSS_SELECTOR, button)

for new_element in range(1, 6):
    click_button.click()
    sleep(2)

button_delete = "button.added-manually"
button_list = driver.find_elements(By.CSS_SELECTOR, button_delete)

print(len(button_list))

sleep(5)
