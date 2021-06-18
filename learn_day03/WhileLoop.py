'''
Add 1 to 10
counter = 1
condition = counter <= 10

while condition:
    block of code till condition is true
    condition modifier
'''
counter = 1
total = 0
while counter <= 10:
    total = total + counter
    print("Counter Value " , counter)
    counter = counter + 1

print("Total of 1 to 10 ", total)
