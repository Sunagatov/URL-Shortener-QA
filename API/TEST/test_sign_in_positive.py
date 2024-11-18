import allure
import pytest
from hamcrest import assert_that, is_not

from API.DATA.user_valid import USER_TO_CREATE
from API.FRAMEWORK.api_endpoints.api_auth import AuthAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code


@allure.feature("6. Sign in (User Authentication)")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignInNegative:
    @allure.title("Check authorization using happy path")
    @allure.description(
        """
        GIVEN user is registered in the system,
        When the user submits a sign-in request with valid email and password,
        THEN HTTP STATUS CODE = 200 and
        AND the system should return a JWT access token and a refresh token"""
    )
    @allure.link("https://shorty-url.atlassian.net/wiki/x/AYAWAQ",
                 name="FR6.1")
    @allure.link("https://team-bov4.testit.software/projects/1/tests", name="Test IT Test-Case #130")
    @pytest.mark.parametrize('sign_up_fixture', USER_TO_CREATE, indirect=True)
    def test_authorization_happy_path(self, sign_up_fixture):
        user_authorization = sign_up_fixture['user_data']
        email = user_authorization[2]
        password = user_authorization[3]
        response_sign_in = AuthAPI().sign_in(email=email, password=password)
        assert_status_code(response=response_sign_in, expected_status_code=200)
        assert_content_type(response=response_sign_in, expected_content_type="application/json")
        token = response_sign_in.json().get("accessToken")
        refresh_token = response_sign_in.json().get("refreshToken")
        assert_that(token, is_not(None), reason="No access token found")
        assert_that(refresh_token, is_not(None), reason="No refresh token found")
