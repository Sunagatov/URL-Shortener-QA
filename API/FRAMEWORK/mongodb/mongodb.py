from allure import step
from pymongo import MongoClient


class MongoDB:
    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        # Connect to MongoDB cluster
        self.mongodb_client = MongoClient(self.connection_string)

    @step('Get all of short url in collection ShortyUrlDb.url_mappings')
    def get_all_short_url(self) -> list:
        with step('Get ShortyUrlDb'):
            shorty_url_db = self.mongodb_client['TestCompany']

        with step('Get url mappings collection'):
            url_mappings_collection = shorty_url_db['TestCollection']

        with step('Get all documents from collection with field shortUrl'):
            documents = url_mappings_collection.find({}, {'shortUrl': 1})

        with step('Get all values of shortUrl fields'):
            short_url_list = [document['shortUrl'] for document in documents if 'shortUrl' in document]
            return short_url_list
