from flask import Flask
from storage.mongo_db import mongo_db_operations
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    # app.run()

    mongo_client = mongo_db_operations.MongoDBOperations()
    mongo_client.get_all_documents()


