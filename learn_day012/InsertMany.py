import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = myclient["testdatabase_july21"]
test_collection = testdb["retail_collection_july21"]
'''
mylist = [
    { "store_number": "0111", "store_name": "Duluth", "address": "111 Duluth Pwky" },
    { "store_number": "0131", "store_name": "Spring Hill", "address": "131 Spring Hill Pkwy" }
]
'''
mylist = [
    {  "_id": 10001, "store_number": "141", "store_name": "Somewhere ", "address": "141 Duluth Pwky" },
    { "_id": 10002, "store_number": "0151", "store_name": "Vinings Hill", "address": "151 Vinings Hill Pkwy" }
]



inserted_records = test_collection.insert_many(mylist)
print(inserted_records.inserted_ids)

myclient.close()

