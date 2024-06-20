import requests
from typing import Tuple
from Auth import Auth
import allure


class Employee:

    def __init__(self, url: str):
        self.url = url
        self.auth = Auth(url)

    @allure.step("Получить список сотрудников компании через АПИ")
    def get_employee_list(self, company_id: int) -> Tuple[list, int]:
        """Получить полный список сотрудников компании

        Args:
            company_id (int): id номер компании

        Returns:
            Tuple[list, int]: список сотрудников и статус код
        """
        employee_list = requests.get(
            self.url + "/employee" + "?company=" + str(company_id)
        )
        return employee_list.json(), employee_list.status_code

    @allure.step("Получить информацию о сотруднике компании через АПИ")
    def get_employee_by_id(self, id: int) -> Tuple[dict, int]:
        """Получить информацию о сотруднике по его ID.

        Args:
            id (int): id номер сотрудника

        Returns:
            Tuple[dict, int]: словарь с информацией о сотруднике и статус код
        """
        result_get_employee_id = requests.get(self.url + "/employee/" + str(id))
        return result_get_employee_id.json(), result_get_employee_id.status_code

    @allure.step("Добавить нового сотрудника в компанию через АПИ")
    def add_new_employee(
        self,
        first_name: str,
        last_name: str,
        company_id: int,
        email: str,
        id_num: int,
        middle_name: str,
        url: str,
        phone: str,
        birthdate: str,
        isActive: bool,
    ) -> Tuple[dict, int]:
        """Добавление нового сотрудника в компанию

        Args:
            first_name (str): имя
            last_name (str): фамилия
            company_id (int): id номер компании
            email (str): адрес электронной почты
            id_num (int): _description_
            middle_name (str): второе имя
            url (str): сайт
            phone (str): номер телефона
            birthdate (str): дата рождения
            isActive (bool): статус

        Returns:
            Tuple[dict, int]: json ответ (c id номером сотрудника) и статус код
        """
        employee_info = {
            "id": id_num,
            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive,
        }
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_add_employee = requests.post(
            self.url + "/employee", json=employee_info, headers=my_token
        )
        return result_add_employee.json(), result_add_employee.status_code

    @allure.step("Изменить информацию о сотруднике через АПИ")
    def edit_employee_info(
        self, id: int, last_name: str, email: str, url: str, phone: str, isActive: bool
    ) -> Tuple[dict, int]:
        """_summary_

        Args:
            id (int): id номер сотрудника
            last_name (str): фамилия
            email (str): адрес электронной почты
            url (str): сайт
            phone (str): номер телефона
            isActive (bool): статус

        Returns:
            Tuple[dict, int]: json ответ (c информацией о сотруднике) и статус код
        """
        employee_new_info = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive,
        }
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_edit_employee_info = requests.patch(
            self.url + "/employee/" + str(id), json=employee_new_info, headers=my_token
        )
        return result_edit_employee_info.json(), result_edit_employee_info.status_code
