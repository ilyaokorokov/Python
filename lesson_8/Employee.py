import requests
from Auth import Auth


class Employee:
    def __init__(self, url):
        self.url = url
        self.auth = Auth(url)

    def get_employee_list(self, company_id):
        employee_list = requests.get(
            self.url + "/employee" + "?company=" + str(company_id)
        )
        return employee_list.json(), employee_list.status_code

    def get_employee_by_id(self, id):
        result_get_employee_id = requests.get(self.url + "/employee/" + str(id))
        return result_get_employee_id.json(), result_get_employee_id.status_code

    def add_new_employee(
        self,
        first_name,
        last_name,
        company_id,
        email,
        # id_num,
        middle_name,
        url,
        phone,
        # birthdate,
        isActive,
    ):
        employee_info = {
            # "id": id_num,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            # "birthdate": birthdate,
            "isActive": isActive,
        }
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_add_employee = requests.post(
            self.url + "/employee", json=employee_info, headers=my_token
        )
        return result_add_employee.json(), result_add_employee.status_code

    def edit_employee_info(self, id, last_name, email, url, phone, isActive):
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
