import allure
import pytest
from allure import step

from API.DATA.user_valid import USER_TO_CREATE
from API.DATA.user_invalid import USER_EMAIL_EMPTY, USER_EMAIL_INVALID, USER_EMAIL_LONG
from API.DATA.user_invalid import USER_PASSWORD_EMPTY, USER_PASSWORD_SHORT, USER_PASSWORD_WITHOUT_UPPERCASE, \
    USER_PASSWORD_WITHOUT_LOWERCASE, USER_PASSWORD_WITHOUT_DIGITS, USER_PASSWORD_WITHOUT_SPEC_CHAR, \
    USER_PASSWORD_WITH_SPACES, USER_PASSWORD_LONG, USER_PASSWORD_INVALID

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
    @pytest.mark.parametrize('sign_up_fixture', USER_EMAIL_LONG, indirect=True)
    def test_email_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Email format is too long'"):
            assert_message_in_response(response, "Email is too long")

    @allure.title("Verify that user can not register with empty password")
    @allure.description(
        """        
        WHEN the user attempts to register with empty password,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must not be empty.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/100", name="Test IT Test-Case #100")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_EMPTY, indirect=True)
    def test_password_empty(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must not be empty'"):
            assert_message_in_response(response, "Password must not be empty")

    @allure.title("Verify that user can not register with too short password")
    @allure.description(
        """        
        WHEN the user attempts to register with too short password,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must be at least 8 characters long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_SHORT, indirect=True)
    def test_password_short(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must be at least 8 characters long'"):
            assert_message_in_response(response, "Password must be at least 8 characters long")

    @allure.title("Verify that user can not register with password without uppercase letter")
    @allure.description(
        """        
        WHEN the user attempts to register with password without uppercase letter,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must contain at least one uppercase letter.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_WITHOUT_UPPERCASE, indirect=True)
    def test_password_without_uppercase(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must contain at least one uppercase letter'"):
            assert_message_in_response(response, "Password must contain at least one uppercase letter")

    @allure.title("Verify that user can not register with password without lowercase letter")
    @allure.description(
        """        
        WHEN the user attempts to register with password without lowercase letter,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must contain at least one lowercase letter.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_WITHOUT_LOWERCASE, indirect=True)
    def test_password_without_lowercase(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must contain at least one lowercase letter'"):
            assert_message_in_response(response, "Password must contain at least one lowercase letter")

    @allure.title("Verify that user can not register with password without digits")
    @allure.description(
        """        
        WHEN the user attempts to register with password without digits,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must contain at least one digit.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_WITHOUT_DIGITS, indirect=True)
    def test_password_without_digits(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must contain at least one digit'"):
            assert_message_in_response(response, "Password must contain at least one digit")

    @allure.title("Verify that user can not register with password without special characters")
    @allure.description(
        """        
        WHEN the user attempts to register with password without special characters,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must contain at least one special character.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.xfail(reason="Bug is not fixed: https://shorty-url.atlassian.net/browse/SHORTY-85", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_WITHOUT_SPEC_CHAR, indirect=True)
    def test_password_without_spec_char(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must contain at least one special character'"):
            assert_message_in_response(response, "Password must contain at least one special character")

    @allure.title("Verify that user can not register with password containing spaces")
    @allure.description(
        """        
        WHEN the user attempts to register with password containing spaces,
        THEN the system should reject the request, 
        AND return an error message indicating that the password must not contain spaces.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_WITH_SPACES, indirect=True)
    def test_password_with_spaces(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password must not contain spaces'"):
            assert_message_in_response(response, "Password must not contain spaces")

    @allure.title("Verify that user can not register with too long password")
    @allure.description(
        """        
        WHEN the user attempts to register with too long password,
        THEN the system should reject the request, 
        AND return an error message indicating that the password is too long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_LONG, indirect=True)
    def test_password_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password is too long'"):
            assert_message_in_response(response, "Password is too long")

    @allure.title("Verify that user can not register with invalid password")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid password,
        THEN the system should reject the request, 
        AND return an error message indicating that the password contains invalid characters.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.3-Password-Constraints-Validation-(Implemented)"), name="FR5.3")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/102", name="Test IT Test-Case #102")
    @pytest.mark.xfail(reason="Bug is not fixed: ", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_PASSWORD_INVALID, indirect=True)
    def test_password_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Password contains invalid characters'"):
            assert_message_in_response(response, "Password contains invalid characters")
