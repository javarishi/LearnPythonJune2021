def shout(text):
    return str(text).upper()

print(shout("This is new method"))
# <class 'function'>
print(type(shout))
test = shout
print(test("This is another test"))