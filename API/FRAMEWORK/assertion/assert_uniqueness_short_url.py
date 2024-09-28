from allure import step
from hamcrest import assert_that, is_not, has_item
from typing import Sequence


@step('Verify that created short url is unique')
def assert_uniqueness_short_url(created_short_url: str, short_url_list: Sequence[str]) -> None:
    assert_that(short_url_list, is_not(has_item(created_short_url)),
                reason='Created short url is not unique')
