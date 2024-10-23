import allure
import pytest
from allure import step
from hamcrest import assert_that, is_not

from API.DATA.user_valid import USER_VALID
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type


@allure.feature("5. Sign up (User Registration)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that user can register")
@allure.description(
    """GIVEN a valid sign-up request,
    WHEN the user submits the sign-up request with valid details,
    THEN the system should create a new user,
    AND return a JWT access token and a refresh token"""
)
@allure.link("https://shorty-url.atlassian.net/wiki/x/EgD4", name="FR")
# @allure.link("https://TestIT", name="Test IT Test-Case #")
@pytest.mark.parametrize('sign_up_fixture', USER_VALID, indirect=True)
def test_sign_up(sign_up_fixture):
    response = sign_up_fixture
    print(response.json())

    with step("Verify status code"):
        assert_status_code(response, 200)

    with step("Verify content-type"):
        assert_content_type(response, "application/json")

    with step("Verify accessToken in the response body"):
        access_token = response.json()['accessToken']
        assert_that(
            access_token,
            is_not(None),
            reason='There is not accessToken field in the response body'
        )

    with step("Verify refreshToken in the response body"):
        refresh_token = response.json()['refreshToken']
        assert_that(
            refresh_token,
            is_not(None),
            reason='There is not refreshToken field in the response body'
        )
