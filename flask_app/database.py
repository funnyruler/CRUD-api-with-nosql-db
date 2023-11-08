import os
from typing import Tuple

import pymongo
import pymongo.errors as pm_errors
from dotenv import load_dotenv
from pymongo.results import InsertOneResult

load_dotenv()


db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
collection_name = os.environ.get('COLLECTION_NAME')
uri = f'mongodb://{db_user}:{db_pass}@{db_host}:{db_port}'


class DataBase:
    def __init__(self):
        self.uri = uri
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_collection(self) -> None:
        try:
            self.db.create_collection(collection_name)
        except pm_errors.CollectionInvalid:  # ignoring exception if collection exists
            pass

    def insert_row(self, data_dict: dict) -> tuple[bool, InsertOneResult] | tuple[bool, str]:
        try:
            result = self.collection.insert_one(data_dict)
            return True, result
        except Exception as e:
            return False, str(e)

    def get_value(self, key: str) -> list:
        documents = self.collection.find({key: {'$exists': True}})
        result = []
        for document in documents:
            result.append(document)
        return result

    def change_value(self, key: dict) -> tuple[bool, str]:
        new_value = key['new_value']
        key_to_change = key['key_to_change']
        change_counter = 0
        values_with_key = self.get_value(key_to_change)
        try:
            for document in values_with_key:
                for key in document:
                    if key == key_to_change:
                        self.collection.find_one_and_update(
                            {"_id": document['_id']},
                            {"$set": {key_to_change: new_value}})
                        change_counter += 1
            return True, str(change_counter)
        except Exception as e:
            # handling unexpected exception
            return False, str(e)
