import pymongo
from pymongo import MongoClient


DB_NAME = "Start_Python"
cluster = MongoClient(
    f"mongodb://localhost:27017/{DB_NAME}")

db = cluster["start_python"]
collection = db["post"]

post = {"_id": "1", "name": "tim", "score": 5}


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

# insert
collection.insert_one(post)
collection.insert_many(posts)

results = collection.find({"title": "morad"})
for result in results:
    print(result)

result2 = collection.find_one({"title": "hanad"})
print(result2)

result3 = collection.find_one({"title": "dash"})
if result3 is None:
    print("Not found")


# Update
collection.update({"_id": "1"}, {"$set": {"name": "sharaf"}})

# post count
postCount = collection.count_documents({})
print(postCount)

# deleted
collection.delete_one({"_id": "1"})

collection.delete_many({})
