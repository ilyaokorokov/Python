from selenium import webdriver
from AuthPage import Auth


def test_auth_form():
    driver = webdriver.Chrome()
    auth_page = Auth(driver)
    auth_page.submit_form(
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "",
        "Москва",
        "Россия",
        "test@skypro.com",
        "+7985899998787",
        "QA",
        "SkyPro",
    )
    auth_page.response_form()
    success_results, danger_results = auth_page.get_result()

    success_class = "alert-success"
    danger_class = "alert-danger"

    for i in success_results:
        assert success_class in i

    for k in danger_results:
        assert danger_class in k

    auth_page._driver.quit()
