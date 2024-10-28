import json
from typing import Optional

import requests
from requests import Response

from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.loggin_allure import log_request
from configs import HOST


class ShorteningLinkAPI:
    def __init__(self):
        """Initializing parameters for request"""
        self.url = f"{HOST}/api/v1/urls"
        self.headers = {"Content-Type": "application/json"}

    def shorten_link(
            self, url: str, days_count: Optional[str] = None, expected_status_code: int = 200
    ) -> Response:
        """Endpoint for creating short link

        Args:
            expected_status_code: expected http status code from response
            url:    original link to shorten;
            days_count: time to expire the short link  in days

        """
        data = {

            "originalUrl": url,
        }
        if days_count is not None:
            data["daysCount"] = days_count
        path = self.url
        response = requests.post(url=path, json=data, headers=self.headers)
        log_request(response)
        return response
