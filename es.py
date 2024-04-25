# Weekly task 07
# Author Cian Gallagher
# Program that reads a txt file in the same directory and prints a count of the letter e it contains.

#The count method is not returning the expected number of es..

FILENAME = "moby-dick.txt"
with open(FILENAME) as f:
    str =  f.read()
    print (str)

    count = str.strip().lower().count("e")
    print(count - 2)