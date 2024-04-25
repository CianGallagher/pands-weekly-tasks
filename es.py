# Weekly task 07
# Author Cian Gallagher
# Program that reads a txt file stated as an argument in command line, counts the occurences of the letter e, and prints out that count.
# sys gives access to sys.argv which is a list of command line arguments passed to a python script. 
import sys

FILENAME = sys.argv[1]
# In this case the FILENAME variable was assigned index 1 as the script itself is index 0. This enables the .txt file to be envoked from the command line in the following format - python es.py .\.moby-dick.txt
with open(FILENAME, 'r') as f:
    str =  f.read()

    #print (str)

    count = str.lower().count("e")

print('The letter e appears in this file',count, 'times.')