import allure
import pytest
import time

from allure import step

from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.assertion.assert_response_header_value import assert_response_header_value
from API.FRAMEWORK.tools.create_short_url import create_short_url
from API.FRAMEWORK.tools.redirect_to_original_url import redirect_to_original_url


@allure.feature("2. Link Redirection")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger!!!Ссылка нерабочая, т.к. не работает сваггер")
class TestRedirection:
    @allure.link("https://team-bov4.testit.software/projects/1/tests/67",
                 name="Test IT Test-Case #67")
    def test_redirection(self):
        original_url = f'https://ya{time.time()}.ru'

        with step('Create short url'):
            created_short_url = create_short_url(original_url)

        redirect_response = redirect_to_original_url(created_short_url)

        with step("Verify status code"):
            assert_status_code(redirect_response, 302)

        assert_response_header_value(redirect_response, 'Location', original_url)

    @allure.link("https://team-bov4.testit.software/projects/1/tests/69",
                 name="Test IT Test-Case #69")
    @pytest.mark.xfail(reason='This feature is not implemented')
    def test_redirection_with_query_params(self):
