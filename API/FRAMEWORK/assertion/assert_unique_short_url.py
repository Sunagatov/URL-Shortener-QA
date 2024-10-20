from typing import Sequence

from allure import step


@step('Verify that created short url is unique')
def is_unique_short_url(created_short_url: str, short_url_list: Sequence[str]) -> None:
    count = short_url_list.count(created_short_url)
    assert count == 1, f'Created short url appears {count} times in the list, expected exactly once.'
