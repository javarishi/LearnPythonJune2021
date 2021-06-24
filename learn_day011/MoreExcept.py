'''
try:
    risky code which may lead to an error
except:
    Logic when exception / error occurs
except Exception:
    Specific First - generic later
    Child First - Parent later
finally:
    executes regardless of error or not
'''
age = input("Please enter your age:")
try:
    int_age = int(age)
    if int_age > 21:
        print("Valid Age for Purchase")
except (ValueError, TypeError) as er:
    print("Invalid Input Provided", er, type(er))
except Exception:
    print("Generic Error unknown at the time of coding")
finally:
    print("Thank You for Considering Our Store")
print("Done!")