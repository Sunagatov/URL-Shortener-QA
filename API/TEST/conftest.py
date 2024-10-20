import os
import pytest
from allure import step
from dotenv import load_dotenv
from hamcrest import assert_that, greater_than

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
