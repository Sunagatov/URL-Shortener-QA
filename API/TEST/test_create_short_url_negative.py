import allure
from allure import step
from hamcrest import is_
import pytest

from API.DATA.original_url_invalid import ORIGINAL_URL_INVALID
from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code


@allure.feature("Short URL generation")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Negative test create short url")
@allure.description(
    """WHEN user send POST request to create short url
       AND original URL is not valid
       THEN status HTTP CODE = 400 and response body contains corresponding error message"""
)
@pytest.mark.parametrize('original_url, error_message', ORIGINAL_URL_INVALID)
def test_create_short_url_negative(original_url, error_message):
    with step("Send POST request to create short url"):
        response = ShorteningLinkAPI().shorten_link(original_url)

    with step("Verify status code"):
        assert_status_code(response, 400)

    with step("Verify content-type"):
        assert_content_type(response, "application/json")

    with step("Verify error message"):
        assert response.json()["errorMessage"], is_(error_message)
