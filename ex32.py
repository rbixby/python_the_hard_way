the_count = [1,2,3,4,5]
fruits = ['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#Same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# We can also built lists, first start with an empty one.
elements = []

# then use the range function to do 0 to 5 counts 
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # use append
    elements.append(i)

# Now we can print these out too
for i in elements:
    print(f"Element was: {i}")

elements_two = list(range(0, 6))

for i in elements_two:
    print(f"Element_two was: {i}")

