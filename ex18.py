"""
    Exercise 18 - Names, Variables, Code, Functions
"""
# this one is like argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nuthin.")

print_two("Roger", "Bixby")
print_two_again("Roger", "Bixby")
print_one("Winning")
print_none()
