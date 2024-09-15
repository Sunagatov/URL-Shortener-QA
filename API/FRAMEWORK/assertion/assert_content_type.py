from hamcrest import assert_that, contains_string
from requests import Response


def assert_content_type(response: Response, expected_content_type: str) -> None:
    """Asserts that the Content-Type of the response matches the expected Content-Type.

    Args:
        response: The response object from the API call.
        expected_content_type: The expected Content-Type string.
    """
    content_type = response.headers.get("Content-Type", "")
    assert_that(
        content_type,
        contains_string(expected_content_type),
        reason=f"Expected Content-Type '{expected_content_type}', found: '{content_type}'",
    )