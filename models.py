from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
database = client["mydatabase"]

users_collection = database["Todo_data"]

async def get_current_database():
    db = database
    yield db

