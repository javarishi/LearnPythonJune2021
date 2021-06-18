int_var = 12
float_var = 12.12
complex_var = 12 + 13j
name = "Niel Armstrong"

print(int_var, type(int_var), id(int_var))
print(float_var, type(float_var), id(float_var))
print(complex_var, type(complex_var), id(complex_var))
print(name, type(name), id(name))

# constructor - initiazlier

age = str(21)
print(age, type(age), id(age))

percentage = 99.45
pc_calc = int(percentage)
print(pc_calc, type(pc_calc))

float_cast = float(int_var)
print(float_cast, type(float_cast))

complex_cast = complex(100)
print(complex_cast, type(complex_cast))
