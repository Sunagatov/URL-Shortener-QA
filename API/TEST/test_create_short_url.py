import pytest
from allure import description
from allure import feature
from allure import step
from allure import title

from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type


@pytest.mark.critical
@feature("Short URL API")
class TestReviewWithRating:

    @title("Test create short url")
    @description(
        "WHEN user send POST request to create short url"
        "THEN status HTTP CODE = 200 and response body contains short url"
    )
    def test_create_short_url(self):
        with step("Send POST request to create short url"):
            original_url = "https://www.google.com"
            response = ShorteningLinkAPI().shorten_link(original_url)
            print(response.json())

        with step("Verify content-type"):
            assert_content_type(response, "application/json")

