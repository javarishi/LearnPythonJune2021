def calculator(num, name):
    function_name = None
    def square():
        return num*num

    def cube():
        return num*num*num

    if name=="square":
        print("square function is selected")
        function_name = square
    else:
        print("cube function is selected")
        function_name= cube
    return function_name

retruned_function = calculator(5, "cube")
print(retruned_function())