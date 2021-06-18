# Sets are written with curly brackets
sampleSet = {"apple", "banana", "pineapple"}
# Add Element: sampleSet.add("mango")
sampleSet.add("mango")
print(sampleSet) # Unordered
sampleSet.add("mango")
print(sampleSet) # Unordered
# Iteration
for eachItem in sampleSet:
    print(eachItem)

if "mango" in sampleSet:
    print("mangos are there")

if "grapes" not in sampleSet:
    print("Grapes arent there")

# Add another set: sampleSet.update(anotherSet)
veggies = {"potatos", "tomatos", "beans", "banana"}
sampleSet.update(veggies)
print(sampleSet)

print(len(sampleSet))
# Remove Element:
sampleSet.remove("banana")
print(sampleSet)
# Discard (No Error) :
sampleSet.discard("apple")

print(sampleSet)
sampleSet.clear()
print(sampleSet)