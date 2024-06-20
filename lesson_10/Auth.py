import requests


class Auth:

    def __init__(self, url: str):
        self.url = url

    def auth_user(self, user: str, password: str) -> str:
        """Авторизация в сервисе

        Args:
            user (str): логин
            password (str): пароль

        Returns:
            str: токен авторизации
        """
        user_info = {"username": "raphael", "password": "cool-but-crude"}
        result_auth = requests.post(self.url + "/auth/login", json=user_info)
        return result_auth.json()["userToken"]
