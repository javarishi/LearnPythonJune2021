import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Database
testdb = myclient["testdatabase_july21"]

# List of Databases in MongoClinet
# print(myclient.list_database_names())

# Collection
test_collection = testdb["retail_collection_july21"]

# Record - Document
oneStore = {
    "store_number": "0121",
    "store_name": "cumberland",
    "address": "121 Cumberland Pwky"
}

inserted_record = test_collection.insert_one(oneStore)
print(inserted_record.inserted_id)



myclient.close()