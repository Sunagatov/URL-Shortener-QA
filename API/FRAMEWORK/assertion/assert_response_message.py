from hamcrest import assert_that, contains_string
from requests import Response


def assert_message_in_response(response: Response, expected_message: str) -> None:
    """Asserts that the message in the response body matches the expected message.

    Args:
        response: The response object from the API call.
        expected_message: The expected message string.
    """
    actual_message = response.json().get("errorMessage", "")
    assert_that(
        actual_message,
        contains_string(expected_message),
        reason=f"Expected response contains '{expected_message}', found: '{actual_message}'",
    )
