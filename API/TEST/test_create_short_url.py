import allure
import pytest
from allure import step
from hamcrest import assert_that, is_, is_not

from API.DATA.loopback_url import LOOPBACK_URL
from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.create_short_url import create_short_url


@allure.feature("Short URL generation")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger")
class TestCreateShortUrl:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test create short url, happy path")
    @allure.description(
        """WHEN user send POST request to create short url   
           THEN status HTTP CODE = 200 and response body contains short url"""
    )
    def test_create_short_url(self):
        with step("Send POST request to create short url"):
            original_url = "https://www.google.com"
            response = ShorteningLinkAPI().shorten_link(original_url)

        with step("Verify status code"):
            assert_status_code(response, 200)

        with step("Verify content-type"):
            assert_content_type(response, "application/json")

        with step("Verify short url"):
            assert response.json()["shortUrl"], is_not(None)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test recreation short url")
    @allure.description(
        """WHEN user send POST request to create short url for the URL already shortened before   
           THEN status HTTP CODE = 200 and response body contains short url with the same short url"""
    )
    def test_recreate_short_url(self):
        with step("Send firstPOST request to create short url"):
            original_url = "https://weather.com/weather/today/l/de8c78996a73470bbe53d7ea51b93a733ee74f0744de3cf7660665e506a33862"
            short_url = create_short_url(original_url)

        with step("Send second POST request to create short url for the origin URL already shortened"):
            response_recreate_short_url = ShorteningLinkAPI().shorten_link(original_url)
            recreated_short_url = response_recreate_short_url.json()["shortUrl"]

        with step(
                "Verify that created short url after second POST request for origin URL is the same as was created before"):
            assert_that(recreated_short_url, is_(short_url),
                        reason="Recreated short url is not the same as was created before")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test recreation short url, happy path")
    @allure.description(
        """WHEN user send POST request to create short url for the URL that points to a loopback address
           THEN status HTTP CODE = 400 and  return an error message indicating that the URL cannot point 
           to a loopback address."""
    )
    @pytest.mark.parametrize('original_url, error_message', LOOPBACK_URL)
    def test_create_short_url_for_loopback_url(self, original_url, error_message):
        with step("Send firstPOST request to create short url for the URL that points to a loopback address"):
            original_url = original_url
            response = ShorteningLinkAPI().shorten_link(original_url)

        with step("Verify status code"):
            assert_status_code(response, 400)

        with step("Verify content-type"):
            assert_content_type(response, "application/json")

        with step("Verify error message"):
            assert response.json()["errorMessage"], is_(error_message)