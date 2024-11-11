import time
from datetime import timedelta

import allure
import pytest
from hamcrest import assert_that

from API.FRAMEWORK.api_endpoints.api_url import UrlAPI
from API.FRAMEWORK.assertion.assert_response_message import assert_message_in_response
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.redirect_to_original_url import redirect_to_original_url
from API.FRAMEWORK.tools.take_hash_from_url import get_url_hash
from API.FRAMEWORK.tools.verification_time_expiration import verify_expiration_date


@allure.feature("Expiration Time")
class TestExpirationTime:
    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.link(
        "https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16023559/4.+Expiration+Time#4.1-Default-Expiration-Time-(Implemented)",
        name="FR4.1")
    @allure.title("Verify that default expiration time of created short url is 365 days from the moment of creation")
    @allure.link(
        "https://team-bov4.testit.software/projects/1/tests/114?isolatedSection=5f9d72fd-d528-4513-9086-6e067c9a2999",
        name="Test IT Test-Case #114")
    @allure.description(
        """
        GIVEN unauthorized user
        WHEN unauthorized user send POST request to create short url without specifying an expiration date   
        THEN default expiration time of created short url is 365 days from the moment of creation"""
    )
    @pytest.mark.parametrize('create_short_url', [f'https://ya{time.time()}.ru'], indirect=True)
    def test_default_expiration_time(self, create_short_url, mongodb_fixture):
        created_short_url = create_short_url["created_short_url"]
        short_url_info = mongodb_fixture.mongodb_client.get_url_info(created_short_url)
        verify_expiration_date(url_info_from_mongodb=short_url_info, expected_days=365)

    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.link(
        "https://team-bov4.testit.software/projects/1/tests?isolatedSection=5f9d72fd-d528-4513-9086-6e067c9a2999",
        name="Test IT Test-Case #124, 125, 117, 122,121")
    @allure.link(
        "https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16023559/4.+Expiration+Time#4.2-Custom-Expiration-Time-(Implemented)",
        name="FR4.2")
    @allure.title("Verify custom expiration time of created short url")
    @allure.description(
        """
        GIVEN unauthorized user
        WHEN unauthorized user send POST request to create short url with specifying an expiration date   
        THEN  expiration time of created short url is equal to the specified date from the moment of creation"""
    )
    @pytest.mark.parametrize(
        'create_short_url',
        [
            ({'original_url': f'https://ya{time.time()}.ru', 'days_count': "30"}),
            ({'original_url': f'https://ya{time.time()}.ru', 'days_count': "364"}),
            ({'original_url': f'https://ya{time.time()}.ru', 'days_count': "2"}),
            ({'original_url': f'https://ya{time.time()}.ru', 'days_count': "1"}),
            ({'original_url': f'https://ya{time.time()}.ru', 'days_count': "365"}),

        ],
        indirect=True
    )
    def test_custom_expiration_time(self, create_short_url, mongodb_fixture):
        created_short_url = create_short_url["created_short_url"]
        days_count = create_short_url["days_count"]
        expected_expiration_days = int(days_count)
        short_url_info = mongodb_fixture.mongodb_client.get_url_info(created_short_url)
        verify_expiration_date(url_info_from_mongodb=short_url_info, expected_days=expected_expiration_days)

    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.link("https://team-bov4.testit.software/projects/1/tests",
                 name="Test IT Test-Case #118, 119, 126")
    @allure.link(
        "https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16023559/4.+Expiration+Time#4.3-Time-Limits-for-Custom-Expiration-(Implemented)",
        name="FR4.3")
    @allure.title("Verify custom expiration time of created short url that is out of range")
    @allure.description(
        """
        GIVEN unauthorized user
        WHEN unauthorized user send POST request to create short url with specifying an expiration date that is out of range   
        THEN  status HTTP CODE = 400 and response body contains error message"""
    )
    @pytest.mark.parametrize(
        'create_short_url, expected_status_code, expected_error_message',
        [
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "0",
                    },
                    400,
                    'Days count must be at least 1 day(s).'
            ),
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "390",
                    },
                    400,
                    'Days count must not exceed 365 day(s).'
            ),
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "366",
                    },
                    400,
                    'Days count must not exceed 365 day(s).'
            )
        ],
        indirect=['create_short_url']
    )
    def test_custom_expiration_time_out_of_range(self, create_short_url, mongodb_fixture,
                                                 expected_status_code, expected_error_message):
        response = create_short_url["response"]
        assert_status_code(response=response, expected_status_code=expected_status_code)
        assert_message_in_response(response=response, expected_message=expected_error_message)

    @pytest.mark.xfail(reason="Not implemented logic to handle invalid dates", run=True)
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.link("https://team-bov4.testit.software/projects/1/tests",
                 name="Test IT Test-Case #120,123")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Verify  expiration time with invalid date")
    @allure.description(
        """
        GIVEN unauthorized user
        WHEN unauthorized user send POST request to create short url with invalid expiration date that is out of range   
        THEN  status HTTP CODE = 400 and response body contains error message"""
    )
    @pytest.mark.parametrize(
        'create_short_url, expected_status_code, expected_error_message',
        [
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "7.5",
                    },
                    400,
                    ' '
            ),
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "-1",
                    },
                    400,
                    'Days count must be at least 1 day(s).'
            ),
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "hello",
                    },
                    400,
                    ' '
            ),
            (
                    {
                        'original_url': f'https://ya{time.time()}.ru',
                        'days_count': "%",
                    },
                    400,
                    ' '
            )
        ],
        indirect=['create_short_url']
    )
    def test_expiration_time_invalid_type(self, create_short_url, mongodb_fixture,
                                          expected_status_code, expected_error_message):
        response = create_short_url["response"]
        assert_status_code(response=response, expected_status_code=expected_status_code)
        assert_message_in_response(response=response, expected_message=expected_error_message)

    @pytest.mark.xfail(reason="Bug, HTTP=302, allows redirection to original url with no error message", run=True)
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.link("https://team-bov4.testit.software/projects/1/tests",
                 name="Test IT Test-Case #116")
    @allure.link(
        "https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16023559/4.+Expiration+Time#4.4-Expired-Short-URLs-(Implemented)",
        name="FR4.4")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Verify  get short url after expiration time ")
    @pytest.mark.parametrize("create_short_url", [(
            {
                'original_url': f'https://www.linkedin.com/jobs/collections/recommended/{time.time()}',
                'days_count': "1",
            })], indirect=True)
    @allure.description(
        """
        GIVEN unauthorized user
        WHEN unauthorized user send GET request short url with expiration TIME  
        THEN  status HTTP CODE = 404 and response body contains error message"""
    )
    def test_verify_get_short_url_after_expiration(self, create_short_url, mongodb_fixture):
        created_short_url = create_short_url["created_short_url"]
        get_hash_from_url = get_url_hash(short_url=created_short_url)
        get_url_info = mongodb_fixture.mongodb_client.get_url_info(created_short_url)
        amount_of_days_to_reduce = 3
        new_expiration_date = get_url_info['expirationDate'] - timedelta(days=amount_of_days_to_reduce)
        mongodb_fixture.mongodb_client.update_expiration_time(
            short_url=created_short_url,
            new_expiration_date=new_expiration_date
        )

        new_created_at_date = get_url_info['createdAt'] - timedelta(days=amount_of_days_to_reduce)
        mongodb_fixture.mongodb_client.update_created_at_time(
            short_url=created_short_url,
            new_created_at=new_created_at_date
        )

        updated_url_info = mongodb_fixture.mongodb_client.get_url_info(created_short_url)
        assert_that(updated_url_info['expirationDate'] == new_expiration_date, "Expiration date was not updated.")
        assert_that(updated_url_info['createdAt'] == new_created_at_date, "createdAt date was not updated.")

        response = redirect_to_original_url(short_url=created_short_url)
        assert_status_code(response=response, expected_status_code=404)
        expected_error_message = f'{{"errorMessage":"Original URL is absent for urlHash=\'{get_hash_from_url}\'"}}'
        assert_message_in_response(response=response, expected_message=expected_error_message)
