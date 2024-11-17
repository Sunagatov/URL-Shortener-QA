import allure
import pytest
import time
from allure import step

from API.DATA.email_invalid import EMAIL_INVALID

from API.FRAMEWORK.api_endpoints.api_auth import AuthAPI
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_response_message import assert_message_in_response


@allure.feature("6. Sign in (User Authentication)")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignInNegative:
    @allure.title("Check authorization using email not existing in the system")
    @allure.description(
        """
        GIVEN an email that does not exist,
        WHEN the user attempts to sign in with that email,
        THEN the system should reject the request 
        AND return an error message indicating that the email is not found.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/18251777/6."
                  "+Sign+in+User+Authentication#6.1-User-Email-Does-Not-Exists-in-the-System-(Implemented)"),
                 name="FR6.1")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/133", name="Test IT Test-Case #133")
    def test_email_not_exist(self):
        email = f'mail{time.time()}.yandex.ru'
        password = 'Password134'

        auth_api = AuthAPI()
        response = auth_api.sign_in(email, password)

        with step("Verify status code is 401"):
            assert_status_code(response, 401)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Invalid email or password'"):
            assert_message_in_response(response, "Invalid email or password")

    @allure.title("Check authorization with an empty email field")
    @allure.description(
        """
        GIVEN a user submits a sign-in request with an empty email,
        WHEN the request is processed,
        THEN the system should reject the request 
        AND return an error message with HTTP status code 400 Bad Request indicating that the email is required.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/18251777/6."
                  "+Sign+in+User+Authentication#6.2.1-Empty-Email"), name="FR6.2.1")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/131", name="Test IT Test-Case #131")
    def test_email_empty(self):
        email = ''
        password = 'Password134'

        auth_api = AuthAPI()
        response = auth_api.sign_in(email, password)

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email must not be empty'"):
            assert_message_in_response(response, "Email must not be empty")

    @allure.title(" Check authorization with an invalid email field")
    @allure.description(
        """
        GIVEN a user submits an email that is invalid (too long, too short, or incorrect format),
        WHEN the request is processed,
        THEN the system should reject the request 
        AND return an error message with HTTP status code 401 Unauthorized 
            indicating that the email or password is invalid.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/18251777/6."
                  "+Sign+in+User+Authentication#6.2.2-Invalid-Email-(Implemented)"), name="FR6.2.2")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/134", name="Test IT Test-Case #134")
    @pytest.mark.parametrize('email_invalid', EMAIL_INVALID)
    def test_email_invalid(self, email_invalid: str):
        email = email_invalid
        password = 'Password134'

        auth_api = AuthAPI()
        response = auth_api.sign_in(email, password)

        with step("Verify status code is 401"):
            assert_status_code(response, 401)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Invalid email or password'"):
            assert_message_in_response(response, "Invalid email or password")
