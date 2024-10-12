
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
    def __init__(self, mongodb_client):
        self.mongodb_client = mongodb_client
        self.created_short_url = None


@pytest.fixture()
def mongodb_fixture() -> MongoDB:
    with step('Create MongoDB client'):
        # Initialize MongoDB with the connection string from the .env file
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_DATABASE_COLLECTION)
        context = MongoDbContext(mongodb_client)
        yield context

    # Clean up after test execution
    if context.created_short_url:
        deleted_count = mongodb_client.delete_created_short_url(context.created_short_url)
        with step('Verify that the created short URL was deleted from MongoDB'):
            assert_that(deleted_count, greater_than(0), reason='Created short URL was not deleted from MongoDB')

    with step('Close MongoDB connection'):
        mongodb_client.close_connection()
