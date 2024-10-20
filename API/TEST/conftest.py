import os
import pytest
from allure import step
from dotenv import load_dotenv
from hamcrest import assert_that, greater_than

from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.api_endpoints.api_url import UrlAPI
from API.FRAMEWORK.assertion.assert_content_type import assert_content_type
from API.FRAMEWORK.assertion.assert_status_code import assert_status_code
from API.FRAMEWORK.mongodb.MongoDB import MongoDB
from configs import MONGODB_DATABASE, MONGODB_DATABASE_COLLECTION

# Load secret config from a .env file:
load_dotenv()
mongodb_uri = os.environ.get('MONGODB_URI')

if not mongodb_uri:
    raise ValueError("MONGO_URI not found in environment variables.")


class MongoDbContext:
    def __init__(self, mongodb_client: 'MongoDB'):
        self.mongodb_client = mongodb_client
        self.created_short_urls = []  # List to track created short URLs


@pytest.fixture()
def mongodb_fixture() -> 'MongoDbContext':
    with step('Create MongoDB client'):
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_DATABASE_COLLECTION)
        context = MongoDbContext(mongodb_client)
        yield context

    # Clean up after test execution
    for short_url in context.created_short_urls:
        deleted_count = context.mongodb_client.delete_created_short_url(short_url)
        with step(f'Verify that the created short URL {short_url} was deleted from MongoDB'):
            assert_that(
                deleted_count,
                greater_than(0),
                reason=f'Created short URL {short_url} was not deleted from MongoDB'
            )

    with step('Close MongoDB connection'):
        context.mongodb_client.close_connection()


@pytest.fixture(scope="function")
def create_short_url(request):
    with step("Send POST request to create short url"):
        original_url = request.param
        response = ShorteningLinkAPI().shorten_link(original_url)

    with step("Get created short url from response body"):
        created_short_url = response.json()["shortUrl"]

    with step("Verify status code"):
        assert_status_code(response, 200)

    with step("Verify content-type"):
        assert_content_type(response, "application/json")

    yield created_short_url, original_url

    with step("Delete created short url"):
        UrlAPI().delete_short_url(created_short_url)
