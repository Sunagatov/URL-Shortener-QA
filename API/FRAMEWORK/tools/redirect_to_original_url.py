import requests
from requests import Response
from allure import step

from API.FRAMEWORK.tools.loggin_allure import log_request


@step('Redirect to original url')
def redirect_to_original_url(short_url: str, query_params: str = '') -> Response:
    url = short_url + query_params
    response = requests.get(url, allow_redirects=False)
    log_request(response)
    return response
