# return_values.py
# Demonstrates returning values and using return in functions

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def is_even(number):
    """Returns True if number is even, False otherwise."""
    return number % 2 == 0

print(multiply(4, 5))
print(is_even(7))