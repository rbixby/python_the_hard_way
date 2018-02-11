"""
    Exercise 33a - While Loops 

    Put the while loop in a functions and add a variable to the upper bound in the while loop
    so that the function will calculate different lists.
"""
def fill_numbers(max):
    numbers = []
    i = 0

    print("******************")
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)
    print("*****************")

fill_numbers(10)
fill_numbers(20)
fill_numbers(4)

