import allure
import time

from allure import step

from API.FRAMEWORK.tools.create_short_url import create_short_url
from API.FRAMEWORK.assertion.assert_unique_short_url import is_unique_short_url


@allure.feature("Short URL generation")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger")
@allure.link("https://team-bov4.testit.software/projects/1/tests/55",
             name="Test IT Test-Case #55")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Verify that created short url is unique")
@allure.description(
        """WHEN user send POST request to create short url   
           THEN created short url is unique"""
    )
def test_uniqueness_short_url(mongodb_fixture):
    original_url = f'https://ya{time.time()}.ru'

    short_url_list = mongodb_fixture.mongodb_client.get_all_short_url()

    with step('Create short url'):
        created_short_url = create_short_url(original_url)

    is_unique_short_url(created_short_url, short_url_list)

    # return created_short_url variable to mongodb_fixture for deleting created short url from MongoDB
    mongodb_fixture.created_short_url = created_short_url
