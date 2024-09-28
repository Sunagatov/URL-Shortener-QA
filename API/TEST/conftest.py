import os
import pytest

from allure import step
from dotenv import load_dotenv
from hamcrest import assert_that, greater_than

from API.FRAMEWORK.mongodb.mongodb import MongoDB
from configs import MONGODB_DATABASE
from configs import MONGODB_DATABASE_COLLECTION


# Load config from a .env file:
load_dotenv()
mongodb_uri = os.environ['MONGODB_URI']


class MongoDbContext:
    def __init__(self, mongodb_client):
        self.mongodb_client = mongodb_client
        self.created_short_url = None


@pytest.fixture()
def mongodb_fixture() -> MongoDB:
    with step('Create MongoDB client'):
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_DATABASE_COLLECTION)
        context = MongoDbContext(mongodb_client)
        yield context

    deleted_count = mongodb_client.delete_created_short_url(context.created_short_url)
    with step('Verify that created short url was deleted from MongoDB'):
        assert_that(deleted_count, greater_than(0),
                    reason='Created short url was not deleted from MongoDB')
