import os

import pytest
from allure import step
from dotenv import load_dotenv
from hamcrest import assert_that, greater_than
from requests import Response

from API.FRAMEWORK.api_endpoints.api_auth import AuthAPI
from API.FRAMEWORK.api_endpoints.api_short_link import ShorteningLinkAPI
from API.FRAMEWORK.mongodb.MongoDB import MongoDB
from configs import MONGODB_DATABASE, MONGODB_COLLECTION_URL, MONGODB_COLLECTION_USER

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
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_COLLECTION_URL)
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
    mongodb_client = None  # Initialize mongodb_client to None
    created_short_url = None  # Initialize created_short_url to None
    with step("Send POST request to create short url"):
        if isinstance(request.param, dict):
            original_url = request.param.get('original_url')
            days_count = request.param.get('days_count')  # Optional parameter
        else:
            original_url = request.param
            days_count = None

        response = ShorteningLinkAPI().shorten_link(url=original_url, days_count=days_count)

        if response.status_code == 200:
            created_short_url = response.json()["shortUrl"]

    yield {
        'response': response,
        'created_short_url': created_short_url,
        'days_count': days_count,
        'original_url': original_url
    }

    if response.status_code == 200:
        with step('Create MongoDB client'):
            mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_COLLECTION_URL)

        deleted_count = mongodb_client.delete_created_short_url(created_short_url)
        with step(f'Verify that the created short URL {created_short_url} was deleted from MongoDB'):
            assert_that(
                deleted_count,
                greater_than(0),
                reason=f'Created short URL {created_short_url} was not deleted from MongoDB'
            )

    # Ensure the MongoDB client is closed if it was created
    if mongodb_client is not None:
        with step('Close MongoDB connection'):
            mongodb_client.close_connection()


@pytest.fixture()
def sign_up_fixture(request) -> Response:
    user_data = request.param
    with step("Create Auth API client"):
        auth_api = AuthAPI()
    response = auth_api.sign_up(*user_data)

    yield {"response": response, "user_data": user_data}

    with step('Create MongoDB client'):
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_COLLECTION_USER)

    email = user_data[2]
    deleted_count = mongodb_client.delete_user(email)

    with step(f'Verify that the created user {user_data[0]} {user_data[1]} was deleted from MongoDB'):
        assert_that(
            deleted_count,
            greater_than(0),
            reason=f'Created user {user_data[0]} {user_data[1]} was not deleted from MongoDB'
        )

    with step('Close MongoDB connection'):
        mongodb_client.close_connection()
