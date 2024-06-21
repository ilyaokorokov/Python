import requests
import allure
from Auth import Auth


class Company:
    def __init__(self, url):
        self.url = url
        self.auth = Auth(url)

    @allure.step("Получить список компаний через АПИ")
    def get_company_list(self) -> list:
        """Метод позволяет получить список компаний

        Returns:
            list: список компаний
        """
        result_company_list = requests.get(self.url + "/company")
        return result_company_list.json()

    @allure.step("Создать организацию через АПИ")
    def create_company(self, name: str, description: str) -> dict:
        """Добавить новую организацию

        Args:
            name (str): название компании
            description (str): описание компании

        Returns:
            dict: словарь с id номером компании
        """
        company_info = {"name": name, "description": description}
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_create_company = requests.post(
            self.url + "/company", json=company_info, headers=my_token
        )
        return result_create_company.json()

    @allure.step("Получить компанию по айди через АПИ")
    def get_company_id(self, id: int) -> dict:
        """Получить информацию об организации по её id номеру

        Args:
            id (int): id номер компании

        Returns:
            dict: словарь с информацией о компании
        """
        result_get_company_id = requests.get(self.url + "/company/" + str(id))
        return result_get_company_id.json()

    @allure.step("Изменить информацию о компании через АПИ")
    def edit_company(self, new_id: int, new_name: str, new_description: str) -> dict:
        """Изменить информацию о компании

        Args:
            new_id (int): id номер компании
            new_name (str): новое название организации
            new_description (str): новое описание организации

        Returns:
            dict: словарь с информацией о компании
        """
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        new_company_info = {"name": new_name, "description": new_description}
        result_edit_company = requests.patch(
            self.url + "/company/" + str(new_id),
            headers=my_token,
            json=new_company_info,
        )
        return result_edit_company.json()

    @allure.step("Удалить компанию через АПИ")
    def delete_company(self, id: int) -> dict:
        """Удалить компанию по её id номеру

        Args:
            id (int): id номер компании

        Returns:
            dict: словарь с информацией об удаленной компании
        """
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_delete_company = requests.get(
            self.url + "/company/delete/" + str(id), headers=my_token
        )
        return result_delete_company.json()

    @allure.step("Активация/деактивация компании через АПИ")
    def set_active_state(self, id: int, isActive: bool) -> dict:
        """Активация/деактивация компании

        Args:
            id (int): id номер компании
            isActive (bool): статус компании (активна/неактивна)

        Returns:
            dict: словарь с информацией о компании
        """
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_active_company = requests.patch(
            self.url + "/company/status/" + str(id),
            headers=my_token,
            json={"isActive": isActive},
        )
        return result_active_company.json()
