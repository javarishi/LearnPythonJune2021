import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = myclient["testdatabase_july21"]
test_collection = testdb["retail_collection_july21"]
'''
x = test_collection.find_one()
print(x)
'''
'''Find Command with Eliminiations 
for eachRecord in test_collection.find({},{'_id':0, 'store_number': 1, 'store_name': 1}):
    print(eachRecord)
'''
# my_query = {'store_number': '0121'}
my_query = {'store_number': { "$gt": "0100" } }
records = test_collection.find(my_query)
for eachRecord in records:
    print(eachRecord)

myclient.close()