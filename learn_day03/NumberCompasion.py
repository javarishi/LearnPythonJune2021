'''
three numbers - find the greatest number
'''
first_var = 1000
second_var = 2000
third_var = 3000
forth_var = 400
'''
four numbers - compare and find greatest 
- no two numbers are equals 
'''

if (first_var > second_var) and (first_var > third_var):
    print("Greatest Variable Value is :" , first_var)
elif second_var > third_var:
    print("Greatest Variable Value is :" , second_var)
else:
    print("Greatest Variable Value is :" , third_var)