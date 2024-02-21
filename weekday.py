# Weekly task 05
# Author Cian Gallagher
# Logic program using datetime module that returns a text output depending on the current day of the week.

# Importing the datetime module enables the use of several useful date related methods.
import datetime

# Defining a function that stores current date as an int and if statement checks.
def is_weekday():
    # Getting the current date, this returns/stores an integer corresponding to the current weekday.
    # The .weekday method stores 0-6 in 'today' depending on current day.
    today = datetime.datetime.now().weekday()

    # If check to determine if it's currently a weekday.
    if today < 5:
        return ' Yes, unfortunately today is a weekday. '
    else:
        return 'It is the weekend, yay!'

# Printing the functions output.
print(is_weekday())