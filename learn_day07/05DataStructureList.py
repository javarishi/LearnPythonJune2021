shopping_cart = ["milk", "veggies", "medicines", 101, 99.7, True]
print(shopping_cart)
print(shopping_cart[0])
print(shopping_cart[0:3])
print(len(shopping_cart))
# Add Element: sampleList.append("newItem")
shopping_cart.append("Universal Remote")
print(shopping_cart)
# Add Indexed Element: sampleList.insert(1, "fruits") - positional access
shopping_cart.insert(1, "fruits")
print(shopping_cart)
# Iterate: for eachItem in sampleList:
for eachItem in shopping_cart:
    print("Iteration " , eachItem)

#Element Exists? : if "apple" in sampleList:
if 101 in shopping_cart:
    print("101 exists")

if 102 not in shopping_cart:
    print("102 not exists")

# Remove Element: sampleList.remove("item")
shopping_cart.remove(101)
print(shopping_cart)
# Remove Indexed Element: sampleList.pop(1)
shopping_cart.pop(0)
print(shopping_cart)
#Using Delete function: del sampleList[0]
del shopping_cart[0]
print(shopping_cart)

# Sorting: sampleList.sort()
simplelist = ["apple", "oranges", "banana", "grapes"]
simplelist.sort()
print(simplelist)

# Clear List: sampleList.clear()
simplelist.clear()
print(simplelist)
