first_var = 1000
second_var = 200
third_var = 300

# AND boolExp1 and boolExp2
'''
S1  S2  S1 and S2
T   T   T
T   F   F
F   T   F
F   F   F
'''
test = (first_var > second_var) and (first_var > third_var)
print("Logical AND " , test)

'''
OR 
S1  S2  S1 or S2
T   T   T
T   F   T
F   T   T
F   F   F
'''
test_or = False or False
print(test_or)

'''
NOT
S1  not S1
T   F
F   T
'''
test_not = not False
print(test_not)
