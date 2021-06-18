# Create a Class
class Customer:

# Constructors in Python
# Can Constructor have parameters?
    def __init__(self, fName="Sample", lName="Test"):
        self.first_name = fName
        self.last_name = lName
        print("Customer is being created", self.first_name, self.last_name)

# Object Methods
    def validate(self, address):
        print("Customer Address Validation", self.first_name, self.last_name)
        self.address = address
        print(self.address)




# Create Object
# instanceName = ClassName()
custOne = Customer("Neil", "ArmStrong")
custTwo = Customer("David","Nix" )
custThree = Customer()

custOne.validate("Smyrna")
print("Customer Two" , custTwo.first_name)
print("Customer Two" , custTwo.last_name)
print("Customer One" , custOne.first_name)
print("Customer One" , custOne.last_name)
# Class / Object functions are instance of method class
print(type(custOne.validate))


