import allure
import pytest
from allure import step

from API.DATA.user_valid import USER_TO_CREATE
from API.DATA.user_invalid import USER_EMAIL_EMPTY, USER_EMAIL_INVALID, USER_EMAIL_LONG
from API.FRAMEWORK.api_endpoints.api_auth import AuthAPI
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_response_message import assert_message_in_response


@allure.feature("5. Sign up (User Registration)")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignUpNegative:
    @allure.title("Verify that user can not register with not unique email")
    @allure.description(
        """
        GIVEN an email that is already in use,
        WHEN the user attempts to register with that email,
        THEN the system should reject the request 
        AND return an error message indicating that the email is already in use.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.1-Unique-Email-Validation-(Implemented)"), name="FR5.1")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/95", name="Test IT Test-Case #95")
    @pytest.mark.xfail(reason="Bug is not fixed: https://shorty-url.atlassian.net/browse/SHORTY-83", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_TO_CREATE, indirect=True)
    def test_unique_email_validation(self, sign_up_fixture):
        auth_api = AuthAPI()
        response = auth_api.sign_up(*USER_TO_CREATE[0])

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email is already in use'"):
            assert_message_in_response(response, "Email is already in use")

    @allure.title("Verify that user can not register with empty email")
    @allure.description(
        """        
        WHEN the user attempts to register with empty email,
        THEN the system should reject the request, 
        AND return an error message indicating that the email must not be empty.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.2-Email-Constraints-Validation-(Implemented)"), name="FR5.2")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/96", name="Test IT Test-Case #96")
    @pytest.mark.parametrize('sign_up_fixture', USER_EMAIL_EMPTY, indirect=True)
    def test_empty_email(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email must not be empty'"):
            assert_message_in_response(response, "Email must not be empty")

    @allure.title("Verify that user can not register with invalid email")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid email,
        THEN the system should reject the request, 
        AND return an error message indicating that the email is invalid.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.2-Email-Constraints-Validation-(Implemented)"), name="FR5.2")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/97", name="Test IT Test-Case #97")
    # @pytest.mark.xfail(reason="Bug is not fixed: https://shorty-url.atlassian.net/browse/SHORTY-83", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_EMAIL_INVALID, indirect=True)
    def test_email_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email format is invalid'"):
            assert_message_in_response(response, "Email format is invalid")

    @allure.title("Verify that user can not register with too long email")
    @allure.description(
        """        
        WHEN the user attempts to register with too long email,
        THEN the system should reject the request, 
        AND return an error message indicating that the email is too long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.2-Email-Constraints-Validation-(Implemented)"), name="FR5.2")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/98", name="Test IT Test-Case #98")
    # @pytest.mark.xfail(reason="Bug is not fixed: https://shorty-url.atlassian.net/browse/SHORTY-83", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_EMAIL_LONG, indirect=True)
    def test_email_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email format is too long'"):
            assert_message_in_response(response, "Email is too long")
