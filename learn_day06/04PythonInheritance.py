class Customer:

    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName
        print("Customer created ", self.first_name, self.last_name)


    def process_promotion(self):
        print("5% discount to ", self.first_name)


class PreferredCustomer(Customer):

    def __init__(self,firstName, lastName, address):
        Customer.__init__(self, firstName, lastName)
        self.address = address
        print("PreferredCustomer ", self.address)

    # if function name is exactly same as Parent class - Override
    def process_promotion(self):
        print("Additional 10% Discount for ", self.first_name)

    def process_email_promotion(self, email):
        print("Email is send to ", self.first_name, email)


cust = Customer("David", "Nix")
cust.process_promotion()
pCust = PreferredCustomer("Neil", "Armstrong" , "Smyrna")
pCust.process_promotion()
pCust.process_email_promotion("neil.moon@nasa.com")