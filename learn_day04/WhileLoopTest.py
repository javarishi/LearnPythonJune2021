'''
while 1 to 20

while condition:
    Loop Logic when condition is true
    condition modifier
'''

count = 1
total = 0
while count <= 20:
    if count == 10:
        count = count + 1
        continue
    print(count)
    total = total + count
    count = count + 1

print("Last Count Value " , count)
print("total is " , total)

'''
How to stop a loop - in between
break
'''

'''
How can I skip an Iteration
continue
'''