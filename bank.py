# Weekly task 02
# Author Cian Gallagher
# Banking program taking two integer inputs from the user and printing their sum in cents.

#Requesting input from user
euroAmountInCents1 = int(input("Please enter the first amount(in cents):"))
euroAmountInCents2 = int(input("Please enter the second amount(in cents):"))

#Storing sum of user inputs in decimal form
decimalResult = (euroAmountInCents1 + euroAmountInCents2) / 100

#Printing result per format provided
print(f'The sum of these amounts is €{decimalResult}')