from hamcrest import assert_that, is_
from requests import Response


def assert_status_code(response: Response, expected_status_code: int) -> None:
    """Asserts that the actual status code matches the expected status code.

    Args:
        response: The response object from the API call.
        expected_status_code: The expected status code.
    """
    assert_that(
        response.status_code,
        is_(expected_status_code),
        reason=f"Expected status code {expected_status_code}, found: {response.status_code}",
    )
