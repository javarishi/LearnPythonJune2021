# Scientific Programming
# Statistics
# Correct results with multiple Iterations
# Fibonacci Series - assignment

def try_recursion(num):
    if num > 0:
        result = num + try_recursion(num - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
try_recursion(10)
