"""
    Exercise 15 - Reading files.

    Zed hasn't mentioned this good practice yet, but I'm a seasoned developer
    and architect, so this is how it's done.
"""
from sys import argv

# Read the script and file name from command line
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the file name again:")
file_again = input('> ')

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
