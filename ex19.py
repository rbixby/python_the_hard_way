"""
    Exercise 19 - Functions and Variables

    This one is designed to show scope. He makes the point here that variables in
    functions are not connected to the variables in the script.

"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket!")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amountOfCheese = 10
amountOfCrackers = 50

cheese_and_crackers(amountOfCheese, amountOfCrackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amountOfCheese + 100, amountOfCrackers + 1000)
