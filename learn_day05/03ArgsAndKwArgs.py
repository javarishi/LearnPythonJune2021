'''
def validate(zipcode, city, county):
    if len(str(zipcode)) == 5:
        print("valid zip code provided ", zipcode)
    else:
        print("Invalid Zip Code")

'''

def validate(first_name, last_name, *args):
    print(first_name, last_name)
    for eachArgs in args:
        print(eachArgs)


def validate2(first_name, last_name,*args, **kwargs):
    print(first_name, last_name)
    print(args, type(args))
    print(kwargs, type(kwargs))


#validate("Neil", "Armstrong", 30080, "Smyrna", "GA")
validate2("Neil", "Armstrong", "abc@xyz.com" , zipcode=30080, county="Smyrna", state="GA")