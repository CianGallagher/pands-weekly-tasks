# Weekly task 06
# Author Cian Gallagher
# A function that approximates the square root of a positive floating point number.
# A tolerance of 1 decimal place is used per task spec example.

def sqrt(n, tolerance = 0.1, iterations = 100):
    #guess being n / 2 is abitrary but is a common starting guess to find a square root.
    guess = n / 2.0

        # This loops the Newton method 'iterations' times.
    for i in range(iterations):
        
        # This is the math behind the Newton method which is looped over.
        guess = 0.5 * (guess + n / guess)
        if round(abs(guess**2 - n), 1) < tolerance:
            return round(guess, 1)

# test output, number of iterations may need to be increased if using a large test number.
testNumberToFindSqrt = 6789.54
result = sqrt(testNumberToFindSqrt)
print(f"The square root of {testNumberToFindSqrt} is approximately {result}")