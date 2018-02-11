"""
    Exercise 21 - Functions can return something
"""
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a , b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} - {b}")
    return a / b

print("Let's do some math with functions!")

age = add(40, 12)
height = subtract(100, 25)
weight = multiply(100, 2)
iq = divide(400, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
