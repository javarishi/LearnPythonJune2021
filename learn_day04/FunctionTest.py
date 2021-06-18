def say_hello(name="Student!"):
    print("Hello ", name)


def validate_address(city, zipcode):
    print(city,zipcode)


def process_tax(shopping_cart):
    for i in shopping_cart:
        print(i)


def square(number):
    return number * number

say_hello("Rishi")
say_hello()
say_hello("Neil")
validate_address("Atlanta", 30080)
shopping_cart = ["milk", "veggies", "medicines", "electronics"]
process_tax(shopping_cart)


print("Square of number ", square(5))