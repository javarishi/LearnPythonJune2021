'''
if condition:
    identify a fault
    raise Error
'''

def validate_age(age):
    int_age = int(age)
    if int_age >= 21:
        print("Valid Age")
    else:
        raise ValueError("Age is not eligible for Purchase")

try:
    validate_age(22)
except ValueError as vr:
    print(vr)