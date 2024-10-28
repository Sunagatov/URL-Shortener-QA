import time

import allure
import pytest

from API.FRAMEWORK.assertion.assert_response_message import assert_message_in_response
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.tools.verification_time_expiration import verify_expiration_date


@allure.feature("Expiration Time")
class TestExpirationTime:
    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Verify that default expiration time of created short url is 365 days from the moment of creation")
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

    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.severity(allure.severity_level.MINOR)
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
            {'original_url': f'https://ya{time.time()}.ru', 'days_count': "30"},

        ],
        indirect=True
    )
    def test_custom_expiration_time(self, create_short_url, mongodb_fixture):
        created_short_url = create_short_url["created_short_url"]
        days_count = create_short_url["days_count"]
        expected_expiration_days = int(days_count)
        short_url_info = mongodb_fixture.mongodb_client.get_url_info(created_short_url)
        verify_expiration_date(url_info_from_mongodb=short_url_info, expected_days=expected_expiration_days)

    @allure.feature("Expiration Time")
    @allure.link("https://short-link.zufargroup.com/api/v1/swagger-ui/index.html",
                 name="Swagger")
    @allure.severity(allure.severity_level.MINOR)
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
