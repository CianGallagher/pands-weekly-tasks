# Weekly task 04
# Author Cian Gallagher
# Mathematical program that applies collatz rules to a positive integer user input, printing each itteration until the number reaches 1

def collatz(n):
    # Run the loop while n does NOT equal 1
    while n != 1:
        print(n)
        # Check if n is even using mod 2, if it is, then divide by 2, if not multiply by 3 and add 1
        if n % 2 == 0:
            # Floor division is used to round down to nearest int after division by 2 to prevent decimal places showing in output   
            n = n // 2
        else:
            n = 3 * n + 1
    # Once n == 1 we leave the loop and print 1        
    print(1)

# Requesting a positive integer input from user
userInput = int(input("Enter a positive integer: "))

# Validating the user input is a positive number
if userInput <= 0:
    print("Please enter a positive integer.")
else:
    # Apply Collatz rules and print the result
    collatz(userInput)