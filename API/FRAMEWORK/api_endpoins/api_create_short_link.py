import json

import requests
from requests import Response

from API.FRAMEWORK.assertions.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.loggin_allure import log_request
from configs import HOST


class ShorteningLinkAPI:
    def __init__(self):
        """Initializing parameters for request"""
        self.url = HOST + "/api/shorten"
        self.headers = {"Content-Type": "application/json"}

    def shorten_link(
        self, url: str,  expected_status_code: int = 200
    ) -> Response:
        """Endpoint for creating short link

        Args:
            expected_status_code: expected http status code from response
            url:    original link to shorten;

        """
        data = {

            "url": url,
        }
        path = self.url
        response = requests.post(url=path, data=json.dumps(data), headers=self.headers)
        assert_status_code(response, expected_status_code=expected_status_code)
        log_request(response)

        return response
