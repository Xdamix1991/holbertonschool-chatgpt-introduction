#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.

    Example:
    factorial(5) returns 120 because 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if an argument is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <non-negative integer>")
    sys.exit(1)

try:
    # Convert the command line argument to an integer
    number = int(sys.argv[1])
    # Ensure the number is non-negative
    if number < 0:
        raise ValueError("The number must be non-negative.")
except ValueError as ve:
    print(ve)
    sys.exit(1)

# Calculate the factorial of the provided number
f = factorial(number)
# Print the result
print(f)
