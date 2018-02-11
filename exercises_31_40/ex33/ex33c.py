"""
    Exercise 33c - While loops

    Rewrite it using a for-loop and the range function. What happens?
"""
def fill_numbers(max, step=1):
    numbers = []
    i = 0

    print("******************")
    for i in range(0, max, step):
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
#fill_numbers(20, 5)
#fill_numbers(4)