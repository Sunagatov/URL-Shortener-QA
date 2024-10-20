from _pytest.fixtures import fixture
from allure import step

from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.api_endpoints.api_url import UrlAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code


@fixture(scope="function")
def create_short_url(request):
    with step("Send POST request to create short url"):
        original_url = request.param
        response = ShorteningLinkAPI().shorten_link(original_url)

    with step("Get created short url from response body"):
        created_short_url = response.json()["shortUrl"]

    with step("Verify status code"):
        assert_status_code(response, 200)

    with step("Verify content-type"):
        assert_content_type(response, "application/json")

    yield created_short_url, original_url

    with step("Delete created short url"):
        UrlAPI().delete_short_url(created_short_url)

