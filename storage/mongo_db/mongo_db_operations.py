"""
Module to handle all the operations related to the MongoDB database.
"""

from pymongo import MongoClient
from storage.database_operations_base import DatabaseOperationsBase

class MongoDBOperations(DatabaseOperationsBase):
    """
    Class to handle all the operations related to the MongoDB database.
    """

    def __init__(self):
        client = MongoClient(CONNECTION_STRING)

    def get_all_documents(self):
        print("test")
        pass

    def get_document_by_id(self, document_id):
        pass

    def create_document_by_id(self, document_id):
        pass

    def update_document_by_id(self, document_id):
        pass

    def mul_update_document_by_id(self, document_id):
        pass

    def delete_document_by_id(self, document_id):
        pass

    def delete_all_documents(self):
        pass

if __name__ == '__main__':
    print("abhigya")