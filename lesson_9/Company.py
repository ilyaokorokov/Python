import requests
from Auth import Auth


class Company:
    def __init__(self, url):
        self.url = url
        self.auth = Auth(url)

    def get_company_list(self, params_to_add=None):
        result_company_list = requests.get(self.url + "/company", params=params_to_add)
        return result_company_list.json()

    def create_company(self, name, description=""):
        company_info = {"name": name, "description": description}
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_create_company = requests.post(
            self.url + "/company", json=company_info, headers=my_token
        )
        return result_create_company.json()

    def get_company_id(self, id):
        result_get_company_id = requests.get(self.url + "/company/" + str(id))
        return result_get_company_id.json()

    def edit_company(self, new_id, new_name, new_description=""):
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        new_company_info = {"name": new_name, "description": new_description}
        result_edit_company = requests.patch(
            self.url + "/company/" + str(new_id),
            headers=my_token,
            json=new_company_info,
        )
        return result_edit_company.json()

    def delete_company(self, id):
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_delete_company = requests.get(
            self.url + "/company/delete/" + str(id), headers=my_token
        )
        return result_delete_company.json()

    def set_active_state(self, id, isActive):
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_active_company = requests.patch(
            self.url + "/company/status/" + str(id),
            headers=my_token,
            json={"isActive": isActive},
        )
        return result_active_company.json()
