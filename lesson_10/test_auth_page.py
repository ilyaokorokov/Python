from selenium import webdriver
from AuthPage import Auth
import allure


@allure.feature("Форма отправки данных")
@allure.title("Тест на заполнение формы")
@allure.description(
    "Заполняем форму тестовыми данными, отправляем, затем считываем результат и сверяем соответствие классов заполненных и незаполненных полей с шаблонами"
)
@allure.severity("Normal")
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
    with allure.step(
        "Считываем информацию с полей формы, после её отправки. Собираем информацию о классах."
    ):
        auth_page.response_form()

        success_results, danger_results = auth_page.get_result()

    with allure.step(
        "Проверяем, что все классы элементов заполненных полей имеют значение - {success_class}, незаполненных полей - {danger_class}"
    ):
        success_class = "alert-success"
        danger_class = "alert-danger"
        with allure.step(
            "В цикле сверяем классы из списка всех заполненных полей с шаблоном"
        ):
            for i in success_results:
                assert success_class in i
        with allure.step(
            "В цикле сверяем классы из списка всех незаполненных полей с шаблоном"
        ):
            for k in danger_results:
                assert danger_class in k

    auth_page._driver.quit()
