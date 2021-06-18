class Customer:

    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName
        print("Customer created ", self.first_name, self.last_name)


    def process_promotion(self):
        print("5% discount to ", self.first_name)


class Person:
    def __init__(self, gender):
        self.gender = gender
        print("Person is Created ", self.gender)


class PreferredCustomer(Customer, Person):

    def __init__(self, firstName, lastName, address, gender):
        Customer.__init__(self, firstName, lastName)
        super().__init__(firstName, lastName)
        Person.__init__(self, gender)
        self.address = address
        print("PreferredCustomer ", self.address)

    # if function name is exactly same as Parent class - Override
    def process_promotion(self):
        print("Additional 10% Discount for ", self.first_name)

    def process_email_promotion(self, email):
        print("Email is send to ", self.first_name, email)


class CreditCardCustomer(PreferredCustomer):
    pass


pCust= PreferredCustomer("Neil", "armstrong", "smyrna", "male")