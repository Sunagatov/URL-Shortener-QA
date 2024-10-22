import requests
from requests import Response
from allure import step

from API.FRAMEWORK.tools.loggin_allure import log_request
from configs import HOST


class AuthAPI:
    def __init__(self):
        self.url = f'{HOST}/api/v1/auth'

    @step('Sign-UP')
    def sign_up(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            country: str,
            age: int
    ) -> Response:
        path = f'{self.url}/signup'
        body = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "country": country,
            "age": age
        }
        response = requests.post(url=path, json=body)
        log_request(response)
        return response
