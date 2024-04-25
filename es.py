# Weekly task 07
# Author Cian Gallagher
# Program that reads a txt file in the same directory, counts the occurences of the letter e, and prints out that count.

FILENAME = "moby-dick.txt"
with open(FILENAME, 'r') as f:
    str =  f.read()
    print (str)

    count = str.lower().count("e")

print('The letter e appears in this file',count, 'times.')