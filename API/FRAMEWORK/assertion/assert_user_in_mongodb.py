import os

from allure import step
from dotenv import load_dotenv
from hamcrest import assert_that, is_

from API.FRAMEWORK.mongodb.MongoDB import MongoDB
from configs import MONGODB_DATABASE, MONGODB_COLLECTION_USER


# Load secret config from a .env file:
load_dotenv()
mongodb_uri = os.environ.get('MONGODB_URI')


@step('Verify that user is in the MongoDB')
def is_user_in_mongodb(email: str) -> None:
    with step('Create MongoDB client'):
        mongodb_client = MongoDB(mongodb_uri, MONGODB_DATABASE, MONGODB_COLLECTION_USER)
    with step(f'Count users with email {email}'):
        count_users = mongodb_client.count_users(email)
    with step('Verify that count users is 1'):
        assert_that(
            count_users,
            is_(1),
            reason='User was not found in MongoDB'
        )
