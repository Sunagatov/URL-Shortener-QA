import allure
import pytest
import time

from allure import step

from API.FRAMEWORK.api_endpoints.api_url import UrlAPI
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.assertion.assert_response_header_value import assert_response_header_value
from API.FRAMEWORK.tools.create_short_url import create_short_url
from API.FRAMEWORK.tools.redirect_to_original_url import redirect_to_original_url


@allure.feature("2. Link Redirection")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger!!!Ссылка нерабочая, т.к. не работает сваггер")
class TestRedirection:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Verify successful redirection to the original URL by a valid short URL")
    @allure.description(
        """WHEN user send GET request to the created short URL   
           THEN response HTTP code is 302
           AND response 'Location' header contains the original URL"""
    )
    @allure.link("https://team-bov4.testit.software/projects/1/tests/67",
                 name="Test IT Test-Case #67")
    def test_redirection(self):
        original_url = f'https://ya{time.time()}.ru'

        with step('Create short url'):
            created_short_url = create_short_url(original_url)

        try:
            redirect_response = redirect_to_original_url(created_short_url)

            with step("Verify status code"):
                assert_status_code(redirect_response, 302)

            assert_response_header_value(redirect_response, 'Location', original_url)

        finally:
            url_api = UrlAPI()
            url_api.delete_short_url(created_short_url)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify successful redirection to the original URL by a valid short URL with query params")
    @allure.description(
        """WHEN user send GET request to the created short URL with query params 
           THEN response HTTP code is 302
           AND response 'Location' header contains the original URL with the same query params"""
    )
    @allure.link("https://team-bov4.testit.software/projects/1/tests/69",
                 name="Test IT Test-Case #69")
    @pytest.mark.xfail(reason='This feature is not implemented', run=True)
    def test_redirection_with_query_params(self):
        original_url = f'https://ya{time.time()}.ru'
        query_params = '?test1=value1&test2=value2'

        with step('Create short url'):
            created_short_url = create_short_url(original_url)

        try:
            redirect_response = redirect_to_original_url(created_short_url, query_params)

            with step("Verify status code"):
                assert_status_code(redirect_response, 302)

            assert_response_header_value(redirect_response, 'Location', original_url + query_params)

        finally:
            UrlAPI().delete_short_url(created_short_url)
