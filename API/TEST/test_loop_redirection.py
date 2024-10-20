import allure
import pytest
from allure import step


from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.redirect_to_original_url import redirect_to_original_url


@allure.feature("2. Link Redirection")
class TestRedirection:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify that loops in URL redirection are avoided")
    @allure.description(
        """WHEN user sends a GET request to the created short URL#1 that is mapped to another short URL#2   
           THEN the response HTTP code is 400
           AND the response body contains the corresponding error message"""
    )
    @pytest.mark.xfail(reason='Bug?', run=True)
    def test_loop_redirection(self, mongodb_fixture):
        with step("Create short url #1"):
            original_url_1 = 'https://example8.com'
            response_1 = ShorteningLinkAPI().shorten_link(original_url_1)
            short_url_1 = response_1.json()['shortUrl']

        with step("Create short url #2"):
            original_url_2 = 'https://example9.com'
            response_2 = ShorteningLinkAPI().shorten_link(original_url_2)
            short_url_2 = response_2.json()['shortUrl']

        with step("Mapping short urls to each other to create a loop"):
            # Register the created short URLs for cleanup
            mongodb_fixture.created_short_urls.extend([short_url_1, short_url_2])

            # Map short URLs to each other to create a loop
            mongodb_fixture.mongodb_client.map_short_urls_bidirectional(short_url1=short_url_1,
                                                                        short_url2=short_url_2,
                                                                        )
        with step("Get short url #1"):
            response = redirect_to_original_url(short_url_1)

        with step("Verify status code"):
            assert_status_code(response, 400)

        with step("Verify error message"):
            assert response.json()['error'] == 'URL cannot point to a loopback address'
