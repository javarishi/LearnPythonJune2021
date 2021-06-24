from learn_day011.BusinessErrors import InvalidAgeError

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
        raise InvalidAgeError("Age is not eligible for Purchase")

try:
    validate_age(12)
except InvalidAgeError as vr:
    print(vr)