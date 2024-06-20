from selenium import webdriver
from OnlineShopPage import OnlineShop
import allure

@allure.feature("Онлайн магазин")
@allure.title("Тест на соответствие цены")
@allure.description("Добавляем в корзину необходимые товары, проверяем итоговую стоимость товаров при оформлении заказа")
@allure.severity("Critical")
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
    with allure.step("Сравниваем стоимость товаров в корзине с ОР"):
        assert total == "Total: $58.29"
    online_shop._driver.quit()
