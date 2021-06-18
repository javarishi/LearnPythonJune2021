"""
Walgreens Store - Customer age is to be validated
for alocohol purchase
18+ - can buy
"""
age = input("Enter Customer Age :")
if age.isdigit():
    int_age = int(age)
    if int_age >= 18:
        print("Allow Alcohol Purchase!")
    else:
        print("Alcohol Purchase is Not Allowed")
else:
    print("Invalid Age Entered")

print("Thank You for Your Purchase")

'''
if condition:
    block of code - when condition is true
else:
    block of code - when condition is false
'''