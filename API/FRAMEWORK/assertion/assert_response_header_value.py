from allure import step
from hamcrest import assert_that, is_
from requests import Response


def assert_response_header_value(response: Response, header: str, expected_header_value: str) -> None:
    with step(f'Verify that header "{header}" has value "{expected_header_value}"'):
        actual_header_value = response.headers.get('Location')
        assert_that(actual_header_value, is_(expected_header_value),
                    reason=f'The "{header}" header has not value "{expected_header_value}"')
