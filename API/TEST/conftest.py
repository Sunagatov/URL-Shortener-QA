import os
import pytest

from allure import step
from dotenv import load_dotenv

from API.FRAMEWORK.mongodb.mongodb import MongoDB


# Load config from a .env file:
load_dotenv()
mongodb_uri = os.environ['MONGODB_URI']


@pytest.fixture()
def mongodb_client() -> MongoDB:
    with step('Create MongoDB client'):
        return MongoDB(mongodb_uri)
