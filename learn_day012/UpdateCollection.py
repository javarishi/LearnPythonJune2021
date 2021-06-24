import pymongo
from future.types import newint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = myclient["testdatabase_july21"]
test_collection = testdb["retail_collection_july21"]

myquery = { "store_number": "0151" }
newvalues = { "$set": { "address": "Canyon 123, Macon" } }

x = test_collection.update_one(myquery, newvalues)
print(x.modified_count)

myclient.close()