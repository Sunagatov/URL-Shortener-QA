import certifi
from pymongo import MongoClient, UpdateOne
from allure import step


class MongoDB:
    def __init__(self, connection_string: str, db_name: str, db_collection: str) -> None:
        self.connection_string = connection_string
        self.db_name = db_name
        self.db_collection = db_collection

        # Connect to MongoDB cluster with SSL certificate verification
        self.mongodb_client = MongoClient(self.connection_string, tls=True, tlsCAFile=certifi.where())

    def close_connection(self) -> None:
        """Close the MongoDB connection."""
        self.mongodb_client.close()

    @step('Delete created short URL from MongoDB')
    def delete_created_short_url(self, created_short_url: str) -> int:
        with step(f'Get {self.db_name}'):
            shorty_url_db = self.mongodb_client[self.db_name]

        with step(f'Get {self.db_collection} collection'):
            url_mappings_collection = shorty_url_db[self.db_collection]

        with step('Delete created short URL'):
            query = {"shortUrl": created_short_url}
            result = url_mappings_collection.delete_one(query)
            return result.deleted_count

    @step('Delete user from MongoDB')
    def delete_user(self, email: str) -> int:
        with step(f'Get {self.db_name}'):
            shorty_url_db = self.mongodb_client[self.db_name]

        with step(f'Get {self.db_collection} collection'):
            user_details_collection = shorty_url_db[self.db_collection]

        with step('Delete user'):
            query = {"email": email}
            result = user_details_collection.delete_one(query)
            return result.deleted_count

    def get_all_short_url(self) -> list:
        """Get all short URLs from the collection."""
        with step(f'Get all of short URL in collection {self.db_name}.{self.db_collection}'):
            with step(f'Get {self.db_name}'):
                shorty_url_db = self.mongodb_client[self.db_name]

            with step(f'Get {self.db_collection} collection'):
                url_mappings_collection = shorty_url_db[self.db_collection]

            with step('Get all documents from collection with field shortUrl'):
                documents = url_mappings_collection.find({}, {'shortUrl': 1})

            with step('Get all values of shortUrl fields'):
                short_url_list = [document['shortUrl'] for document in documents if 'shortUrl' in document]
                return short_url_list

    @step('Map two short URLs to each other bidirectionally in MongoDB')
    def map_short_urls_bidirectional(self, short_url1: str, short_url2: str) -> None:
        with step(f'Get {self.db_name} database'):
            db = self.mongodb_client[self.db_name]

        with step(f'Get {self.db_collection} collection'):
            url_mappings_collection = db[self.db_collection]

        with step('Update documents to map short URLs bidirectionally'):
            # Use short_url1 and short_url2 directly since they are already full URLs
            operations = [
                UpdateOne(
                    {"shortUrl": short_url1},  # Query using the 'shortUrl' field
                    {"$set": {"originalUrl": short_url2}}  # Set 'originalUrl' to the other full URL
                ),
                UpdateOne(
                    {"shortUrl": short_url2},
                    {"$set": {"originalUrl": short_url1}}
                )
            ]

            # Execute the bulk write operation
            result = url_mappings_collection.bulk_write(operations)

            # Check if both updates were successful
            if result.matched_count < 2:
                missing_urls = []
                if result.matched_count == 0:
                    missing_urls = [short_url1, short_url2]
                elif result.matched_count == 1:
                    # One of the URLs was not found
                    missing_urls = [short_url1] if result.modified_count == 0 else [short_url2]
                raise ValueError(f"Mapping failed: Short URLs not found: {', '.join(missing_urls)}")

            # Optionally, return the result
            return result

    def verify_mappings(self, short_url1: str, short_url2: str):
        db = self.mongodb_client[self.db_name]
        url_mappings_collection = db[self.db_collection]

        doc1 = url_mappings_collection.find_one({"shortUrl": short_url1})
        doc2 = url_mappings_collection.find_one({"shortUrl": short_url2})

        print(f"Document for {short_url1}: {doc1}")
        print(f"Document for {short_url2}: {doc2}")
