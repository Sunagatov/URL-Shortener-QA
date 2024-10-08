import requests
from requests import Response
from allure import step

from API.FRAMEWORK.tools.loggin_allure import log_request
from configs import HOST


class UrlAPI:
    def __init__(self):
        self.url = f'{HOST}/api/v1/url'

    @step('Delete short URL')
    def delete_short_url(self, short_url: str) -> Response:
        with step('Get short URL hash'):
            short_url_hash = short_url.rsplit('/', 1)[-1]

        with step('Send request to delete short URL'):
            path = f'{self.url}/{short_url_hash}'
            response = requests.delete(url=path)
            log_request(response)
            return response
