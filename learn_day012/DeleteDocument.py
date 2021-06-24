import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = myclient["testdatabase_july21"]
test_collection = testdb["retail_collection_july21"]

myquery = { "store_number" : "0121" }

x  = test_collection.delete_one(myquery)
print(x.deleted_count, "records deleted")


myclient.close()