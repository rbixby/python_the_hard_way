my_name = 'Roger W. Bixby'
my_age = 52 # True unfortunately
my_height = 66 # In inches
my_height_cm = round(my_height * 2.54,2)
my_weight = 215
my_weight_kg = round(my_weight * (1/2.2),2)
my_eyes = 'Green'
my_teeth = 'Yellowish white'
my_hair = 'Red'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_height_cm} centimeters tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"He's {my_weight_kg} kilograms heavy.")
print("Actually that's not too heavy for someone taller.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky so make sure to get it right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
