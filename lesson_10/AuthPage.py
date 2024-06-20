from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Auth:

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step(
        "Внести данные в форму отправки и отправить её. {first_name}, {last_name}, {address}, {zip_code}, {city}, {country}, {e_mail}, {phone_number}, {job_position}, {company}"
    )
    def submit_form(
        self,
        first_name: str,
        last_name: str,
        address: str,
        zip_code: str,
        city: str,
        country: str,
        e_mail: str,
        phone_number: str,
        job_position: str,
        company: str,
    ):
        """
        Данный метод получает на вход контактные данные, вносит их в
        соответствующие поля и отправляет заполненную форму

        Args:
            first_name (str): имя
            last_name (str): фамилия
            address (str): адрес
            zip_code (str): почтовый индекс
            city (str): город
            country (str): страна
            e_mail (str): адрес электронной почты
            phone_number (str): номер телефона
            job_position (str): должность
            company (str): название организации
        """

        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]'
        ).send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(
            last_name
        )
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(
            address
        )
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(
            e_mail
        )
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(
            phone_number
        )
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(
            zip_code
        )
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(
            country
        )
        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]'
        ).send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(
            company
        )
        self._driver.find_element(
            By.CSS_SELECTOR, 'button.btn-outline-primary[type="submit"]'
        ).click()

    def response_form(self):
        """
        Данный метод считывает информацию с полей формы, после её отправки
        """
        self.first_name_new = self._driver.find_element(By.CSS_SELECTOR, "#first-name")
        self.last_name_new = self._driver.find_element(By.CSS_SELECTOR, "#last-name")
        self.address_new = self._driver.find_element(By.CSS_SELECTOR, "#address")
        self.e_mail_new = self._driver.find_element(By.CSS_SELECTOR, "#e-mail")
        self.phone_number_new = self._driver.find_element(By.CSS_SELECTOR, "#phone")
        self.zip_code_new = self._driver.find_element(By.CSS_SELECTOR, "#zip-code")
        self.city_new = self._driver.find_element(By.CSS_SELECTOR, "#city")
        self.country_new = self._driver.find_element(By.CSS_SELECTOR, "#country")
        self.job_position_new = self._driver.find_element(
            By.CSS_SELECTOR, "#job-position"
        )
        self.company_new = self._driver.find_element(By.CSS_SELECTOR, "#company")

    @allure.step("Сохраняем в списки классы заполненных и незаполненных полей")
    def get_result(self) -> list:
        """Данный метод сохраняет в списки классы заполненных и незаполненных полей.

        Returns:
            list: 2 списка с классами полей
        """
        success_results = []
        danger_results = []

        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )
        fields = [
            self.first_name_new,
            self.last_name_new,
            self.address_new,
            self.e_mail_new,
            self.phone_number_new,
            self.city_new,
            self.country_new,
            self.job_position_new,
            self.company_new,
        ]

        for element in fields:
            result = element.get_attribute("class")
            success_results.append(result)

        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger"))
        )
        danger_element = self.zip_code_new.get_attribute("class")
        danger_results.append(danger_element)

        return success_results, danger_results
