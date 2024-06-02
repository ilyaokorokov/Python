from selenium.webdriver.common.by import By


class OnlineShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def user_auth(self, username: str, password: str):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def get_info_and_buttons(self):
        self.add_to_cart = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory"
        )
        self.item_names = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_name"
        )
        self.prices = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_price"
        )

    def add_items_to_cart(self, name_item1: str, name_item2: str, name_item3: str):
        item1_button = None
        item2_button = None
        item3_button = None

        for i in range(len(self.item_names)):
            item = self.item_names[i]
            if item.text == name_item1 and not item1_button:
                item1_button = self.add_to_cart[i]
            elif item.text == name_item2 and not item2_button:
                item2_button = self.add_to_cart[i]
            elif item.text == name_item3 and not item3_button:
                item3_button = self.add_to_cart[i]

        if item1_button and item2_button and item3_button:
            item1_button.click()
            item2_button.click()
            item3_button.click()

    def place_order(self, first_name: str, last_name: str, zip_code: str):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_result_price(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text
        return total
