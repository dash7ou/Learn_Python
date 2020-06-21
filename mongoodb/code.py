import pymongo
from pymongo import MongoClient

DB_NAME = "Start_Python"
cluster = MongoClient(
    f"mongodb://localhost:27017/{DB_NAME}")

db = cluster["start_python"]
collection = db["post"]

post = {"name": "tim", "score": 5}

collection.insert_one(post)

posts = [
    {
        "title": "morad",
        "likes": 6
    },
    {
        "title": "hanad",
        "likes": 10
    }
]


collection.insert_many(posts)
