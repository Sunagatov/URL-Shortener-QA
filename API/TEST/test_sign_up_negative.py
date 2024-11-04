import allure
import pytest
from allure import step

from API.DATA.user_valid import USER_TO_CREATE
from API.DATA.user_invalid import (USER_EMAIL_EMPTY, USER_EMAIL_INVALID, USER_EMAIL_LONG,
                                   USER_PASSWORD_EMPTY, USER_PASSWORD_SHORT, USER_PASSWORD_WITHOUT_UPPERCASE,
                                   USER_PASSWORD_WITHOUT_LOWERCASE, USER_PASSWORD_WITHOUT_DIGITS,
                                   USER_PASSWORD_WITHOUT_SPEC_CHAR, USER_PASSWORD_WITH_SPACES, USER_PASSWORD_LONG,
                                   USER_PASSWORD_INVALID,
                                   USER_FIRST_NAME_EMPTY, USER_FIRST_NAME_INVALID, USER_FIRST_NAME_LONG,
                                   USER_LAST_NAME_EMPTY, USER_LAST_NAME_INVALID, USER_LAST_NAME_LONG,
                                   USER_COUNTRY_EMPTY, USER_COUNTRY_INVALID, USER_COUNTRY_LONG,
                                   USER_AGE_INVALID, USER_AGE_NOT_NUMBER)

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
    def test_email_unique_validation(self, sign_up_fixture):
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
    def test_email_empty(self, sign_up_fixture):
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

    @allure.title("Verify that user can not register with empty first name")
    @allure.description(
        """        
        WHEN the user attempts to register with empty first name,
        THEN the system should reject the request, 
        AND return an error message indicating that the first name must not be empty.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.4-First-Name-Constraints-Validation-(Implemented)"), name="FR5.4")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/105", name="Test IT Test-Case #105")
    @pytest.mark.parametrize('sign_up_fixture', USER_FIRST_NAME_EMPTY, indirect=True)
    def test_first_name_empty(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'First name must not be empty'"):
            assert_message_in_response(response, "First name must not be empty")

    @allure.title("Verify that user can not register with invalid first name")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid first name,
        THEN the system should reject the request, 
        AND return an error message indicating that the first name contains invalid characters.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.4-First-Name-Constraints-Validation-(Implemented)"), name="FR5.4")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/107", name="Test IT Test-Case #107")
    @pytest.mark.parametrize('sign_up_fixture', USER_FIRST_NAME_INVALID, indirect=True)
    def test_first_name_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'First name contains invalid characters'"):
            assert_message_in_response(response, "First name contains invalid characters")

    @allure.title("Verify that user can not register with too long first name")
    @allure.description(
        """        
        WHEN the user attempts to register with too long first name,
        THEN the system should reject the request, 
        AND return an error message indicating that the first name is too long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.4-First-Name-Constraints-Validation-(Implemented)"), name="FR5.4")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/107", name="Test IT Test-Case #107")
    @pytest.mark.parametrize('sign_up_fixture', USER_FIRST_NAME_LONG, indirect=True)
    def test_first_name_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'First name is too long'"):
            assert_message_in_response(response, "First name is too long")

    @allure.title("Verify that user can not register with empty last name")
    @allure.description(
        """        
        WHEN the user attempts to register with empty last name,
        THEN the system should reject the request, 
        AND return an error message indicating that the last name must not be empty.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.5-Last-Name-Constraints-Validation-(Implemented)"), name="FR5.5")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/108", name="Test IT Test-Case #108")
    @pytest.mark.parametrize('sign_up_fixture', USER_LAST_NAME_EMPTY, indirect=True)
    def test_last_name_empty(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Last name must not be empty'"):
            assert_message_in_response(response, "Last name must not be empty")

    @allure.title("Verify that user can not register with invalid last name")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid last name,
        THEN the system should reject the request, 
        AND return an error message indicating that the last name contains invalid characters.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.5-Last-Name-Constraints-Validation-(Implemented)"), name="FR5.5")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/110", name="Test IT Test-Case #110")
    @pytest.mark.parametrize('sign_up_fixture', USER_LAST_NAME_INVALID, indirect=True)
    def test_last_name_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Last name contains invalid characters'"):
            assert_message_in_response(response, "Last name contains invalid characters")

    @allure.title("Verify that user can not register with too long last name")
    @allure.description(
        """        
        WHEN the user attempts to register with too long last name,
        THEN the system should reject the request, 
        AND return an error message indicating that the last name is too long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.5-Last-Name-Constraints-Validation-(Implemented)"), name="FR5.5")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/110", name="Test IT Test-Case #110")
    @pytest.mark.parametrize('sign_up_fixture', USER_LAST_NAME_LONG, indirect=True)
    def test_last_name_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Last name is too long'"):
            assert_message_in_response(response, "Last name is too long")

    @allure.title("Verify that user can not register with empty country")
    @allure.description(
        """        
        WHEN the user attempts to register with empty country,
        THEN the system should reject the request, 
        AND return an error message indicating that the country name must not be empty.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.6-Country-Constraints-Validation-(Implemented)"), name="FR5.6")
    # @allure.link("https://team-bov4.testit.software/projects/1/tests/113", name="Test IT Test-Case #113")
    @pytest.mark.parametrize('sign_up_fixture', USER_COUNTRY_EMPTY, indirect=True)
    def test_country_empty(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Country name must not be empty'"):
            assert_message_in_response(response, "Country name must not be empty")

    @allure.title("Verify that user can not register with invalid country")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid country,
        THEN the system should reject the request, 
        AND return an error message indicating that the country contains invalid characters.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.6-Country-Constraints-Validation-(Implemented)"), name="FR5.6")
    # @allure.link("https://team-bov4.testit.software/projects/1/tests/113", name="Test IT Test-Case #113")
    @pytest.mark.parametrize('sign_up_fixture', USER_COUNTRY_INVALID, indirect=True)
    def test_country_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Country name contains invalid characters'"):
            assert_message_in_response(response, "Country name contains invalid characters")

    @allure.title("Verify that user can not register with too long country")
    @allure.description(
        """        
        WHEN the user attempts to register with too long country,
        THEN the system should reject the request, 
        AND return an error message indicating that the country name is too long.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.6-Country-Constraints-Validation-(Implemented)"), name="FR5.6")
    # @allure.link("https://team-bov4.testit.software/projects/1/tests/113", name="Test IT Test-Case #113")
    @pytest.mark.parametrize('sign_up_fixture', USER_COUNTRY_LONG, indirect=True)
    def test_country_long(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Country name is too long'"):
            assert_message_in_response(response, "Country name is too long")

    @allure.title("Verify that user can not register with invalid age")
    @allure.description(
        """        
        WHEN the user attempts to register with invalid age,
        THEN the system should reject the request, 
        AND return an error message indicating that the age must be between 13 and 120.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.7-Age-Constraints-Validation-(Implemented)"), name="FR5.7")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/111", name="Test IT Test-Case #111")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/113", name="Test IT Test-Case #113")
    @pytest.mark.parametrize('sign_up_fixture', USER_AGE_INVALID, indirect=True)
    def test_age_invalid(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Age must be between 13 and 120'"):
            assert_message_in_response(response, "Age must be between 13 and 120")

    @allure.title("Verify that user can not register with not a number age")
    @allure.description(
        """        
        WHEN the user attempts to register with not a number age,
        THEN the system should reject the request, 
        AND return an error message indicating that the age must be a valid integer.
        """
    )
    @allure.link(("https://shorty-url.atlassian.net/wiki/spaces/SKB/pages/16252946/5."
                  "+Sign+up+User+Registration#5.7-Age-Constraints-Validation-(Implemented)"), name="FR5.7")
    @allure.link("https://team-bov4.testit.software/projects/1/tests/113", name="Test IT Test-Case #113")
    @pytest.mark.xfail(reason="Bug is not fixed: https://shorty-url.atlassian.net/browse/SHORTY-87", run=True)
    @pytest.mark.parametrize('sign_up_fixture', USER_AGE_NOT_NUMBER, indirect=True)
    def test_age_not_number(self, sign_up_fixture):
        response = sign_up_fixture["response"]

        with step("Verify status code is 400"):
            assert_status_code(response, 400)

        with step("Verify content-type is 'application/json'"):
            assert_content_type(response, "application/json")

        with step("Verify response message is 'Age must be a valid integer'"):
            assert_message_in_response(response, "Age must be a valid integer")
