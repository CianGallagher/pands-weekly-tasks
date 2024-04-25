# Weekly task 03
# Author Cian Gallagher
# Accounts program taking a 10 digit account number from the user and printing the banking standard redacted output.
# Account number inputs with fewer than 5 length will not be redacted as these would fall outside typical banking standards.

def account_number_redacted(accountNumberUserInput):

    # Change all digits to X apart from the final 4 using the users input length. 
    redactedOutput = 'X' * (len(accountNumberUserInput) - 4) + accountNumberUserInput[-4:]

    # Print the redacted account number
    print("Redacted account number:", redactedOutput)

# Get user input for account number and store it in accountNumberUserInput
accountNumberUserInput = input("Enter your account number: ")

# Call the function using the user input as the argument
account_number_redacted(accountNumberUserInput)
