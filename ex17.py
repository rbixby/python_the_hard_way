"""
    Exercise 17 - More files

    This one copies a file to another files

"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# We could do these two on one line, how?
inFile = open(from_file)
inData = inFile.read()

print(f"The input file is {len(inData)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

outFile = open(to_file, 'w')
outFile.write(inData)

print("Alright, all done.")

inFile.close()
outFile.close()
