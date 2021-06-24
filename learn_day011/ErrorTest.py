'''
try:
    risky code which may lead to an error
except:
    Logic when exception / error occurs
finally:
    executes regardless of error or not
'''
age = input("Please enter your age:")
try:
    int_age = int(age)
    if int_age > 21:
        print("Valid Age for Purchase")
except ValueError:
    print("Invalid Input Provided")
finally:
    print("Thank You for Considering Our Store")
print("Done!")