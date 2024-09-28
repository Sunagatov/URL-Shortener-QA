import allure
import time


from API.FRAMEWORK.tools.create_short_url import create_short_url
from API.FRAMEWORK.assertion.assert_uniqueness_short_url import assert_uniqueness_short_url


@allure.feature("Short URL generation")
@allure.link("https://short-link.zufargroup.com/webjars/swagger-ui/index.html#/URL%20Shortening/shortenUrl",
             name="Swagger")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that created short url is unique")
@allure.description(
        """WHEN user send POST request to create short url   
           THEN created short url is unique"""
    )
def test_uniqueness_short_url(mongodb_client):
    original_url = f'https://ya{time.time()}.ru'

    short_url_list = mongodb_client.get_all_short_url()

    with allure.step('Create short url'):
        created_short_url = create_short_url(original_url)

    assert_uniqueness_short_url(created_short_url, short_url_list)
