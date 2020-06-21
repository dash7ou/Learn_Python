import pymongo
from pymongo import MongoClient

DB_NAME = "Start_Python"
cluster = MongoClient(
    f"mongodb://localhost:27017/{DB_NAME}")

db = cluster["start_python"]
collection = db["post"]

post = {"name": "tim", "score": 5}

# collection.insert_one(post)

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


# collection.insert_many(posts)

results = collection.find({"title": "morad"})
for result in results:
    print(result)

result2 = collection.find_one({"title": "hanad"})
print(result2)

result3 = collection.find_one({"title": "dash"})
if result3 is None:
    print("Not found")
