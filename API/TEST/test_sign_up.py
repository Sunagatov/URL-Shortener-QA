import allure
import pytest

from API.DATA.user_valid import USER_VALID


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
@pytest.mark.parametrize('user_data', USER_VALID, indirect=True)
def test_sign_up(user_data, sign_up):
    response = sign_up
    print(response.json())
