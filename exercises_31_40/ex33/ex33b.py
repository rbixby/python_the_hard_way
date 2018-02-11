"""
    Exercise 33b - While Loops

    Now add a second parameter to the function to change the step.
"""
def fill_numbers(max, step=1):
    numbers = []
    i = 0

    print("******************")
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)
    print("*****************")

fill_numbers(10)
fill_numbers(20, 5)
fill_numbers(4)