from allure import step
from pymongo import MongoClient


class MongoDB:
    def __init__(self, connection_string: str, db_name: str, db_collection: str) -> None:
        self.connection_string = connection_string
        self.db_name = db_name
        self.db_collection = db_collection
        # Connect to MongoDB cluster
        self.mongodb_client = MongoClient(self.connection_string)

    def close_connection(self) -> None:
        self.mongodb_client.close()

    @step('Delete created short url from MongoDB')
    def delete_created_short_url(self, created_short_url: str) -> int:
        with step(f'Get {self.db_name}'):
            shorty_url_db = self.mongodb_client[self.db_name]

        with step(f'Get {self.db_collection} collection'):
            url_mappings_collection = shorty_url_db[self.db_collection]

        with step('Delete created short url'):
            query = {"shortUrl": created_short_url}
            result = url_mappings_collection.delete_one(query)
            return result.deleted_count

    def get_all_short_url(self) -> list:
        with step(f'Get all of short url in collection {self.db_name}.{self.db_collection}'):
            with step(f'Get {self.db_name}'):
                shorty_url_db = self.mongodb_client[self.db_name]

            with step(f'Get {self.db_collection} collection'):
                url_mappings_collection = shorty_url_db[self.db_collection]

            with step('Get all documents from collection with field shortUrl'):
                documents = url_mappings_collection.find({}, {'shortUrl': 1})

            with step('Get all values of shortUrl fields'):
                short_url_list = [document['shortUrl'] for document in documents if 'shortUrl' in document]
                return short_url_list
