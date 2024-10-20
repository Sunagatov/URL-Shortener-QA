import requests
from allure_commons._allure import step
from requests import Response

from API.FRAMEWORK.tools.loggin_allure import log_request
from configs import HOST

from urllib.parse import urljoin


class GetShortUrlAPI:
    def __init__(self):
        # Ensure HOST does not end with a slash
        self.base_url = HOST.rstrip('/')

    @step('Get short URL')
    def get_short_url(self, short_url: str, allow_redirects=False) -> Response:
        with step('Extract short URL hash'):
            # Extract the last part of the URL
            short_url_hash = short_url.rsplit('/', 1)[-1]

        with step('Construct full URL for GET request'):
            # Construct the URL correctly using urljoin
            path = urljoin(f'{self.base_url}/', short_url_hash)
            print(f'Requesting URL: {path}')

        with step('Send request to get short URL'):
            response = requests.get(url=path, allow_redirects=allow_redirects)
            log_request(response)
            return response
