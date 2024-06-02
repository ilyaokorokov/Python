from selenium import webdriver
from OnlineShopPage import OnlineShop


def test_online_shop():
    driver = webdriver.Chrome()
    online_shop = OnlineShop(driver)
    online_shop.user_auth("standard_user", "secret_sauce")
    online_shop.get_info_and_buttons()
    online_shop.add_items_to_cart(
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
    )
    online_shop.place_order("Илья", "Окороков", "350024")
    total = online_shop.get_result_price()
    assert total == "Total: $58.29"
    online_shop._driver.quit()
