import requests


class Auth:
    def __init__(self, url):
        self.url = url

    def auth_user(self, user="raphael", password="cool-but-crude"):
        user_info = {"username": user, "password": password}
        result_auth = requests.post(self.url + "/auth/login", json=user_info)
        return result_auth.json()["userToken"]
