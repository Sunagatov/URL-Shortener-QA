import requests
from requests import Response
from allure import step


@step('Redirect to original url')
def redirect_to_original_url(short_url: str) -> Response:
    response = requests.get(short_url, allow_redirects=False)
    return response
