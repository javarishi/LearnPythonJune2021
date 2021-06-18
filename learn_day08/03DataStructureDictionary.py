# Dictionaries are written in Curly Braces { "Key" : "value"}
sampleDictionary ={
    "storeID" : "0121",
    "store_name" : "Cumlerland Store",
    "estd" : 2000,
    "testList" : [101, 102, 103],
    "testDict" : {"key1": "value1", "key2" : "value2"}
}
print(sampleDictionary)
# Access with Get:
print(sampleDictionary.get("storeID"))
# Add key value pair:
sampleDictionary["address"] = "0121 Cumberland Pwky"
print(sampleDictionary)

'''
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))
'''
for key, value in sampleDictionary.items():
    print(key, value)

#Iterate  just Value :
for eachValue in sampleDictionary.values():
    print(eachValue)

if "estd" in sampleDictionary:
    print("estd key exists")

if 2000 in sampleDictionary.values():
    print(2000, "exits")

print(len(sampleDictionary))

# Remove Last Added Item:
sampleDictionary.popitem()
print(sampleDictionary)

sampleDictionary.pop("estd")
print(sampleDictionary)

sampleDictionary.clear()
print(sampleDictionary)