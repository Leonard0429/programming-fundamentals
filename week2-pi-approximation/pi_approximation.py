# This function calculates one term of the series
def calcTerm(denominator):
    # Each term is 4 divided by the denominator
    return 4 / denominator

# This function calculates the approximation of pi using x terms
def calcPi(x):
    pi_approx = 0       # Start with 0
    sign = 1            # First term is positive
    denominator = 1     # First denominator is 1

    # Repeat x times to calculate x terms
    for i in range(x):
        term = calcTerm(denominator)   # Get the term value
        pi_approx += sign * term       # Add or subtract the term
        sign *= -1                     # Flip the sign for next term
        denominator += 2               # Move to the next odd number

    return pi_approx

# This is the main program
def main():
    # Ask the user to enter how many terms to use
    x = int(input("Enter how many terms to use to approximate pi (must be at least 1): "))

    # Check if the input is valid
    if x < 1:
        print("Please enter a number 1 or more.")
        return  # Stop the program if input is invalid

    # Call the function to calculate pi
    result = calcPi(x)

    # Show the result
    print("Approximation of pi using", x, "terms is:", result)

# Run the main program
main()
