# basic_functions.py
# Example 1: Simple function definition and calling

def greet():
    """Prints a simple greeting."""
    print("Hello, welcome to Python Functions!")

# Function call
greet()


# Example 2: Function with parameters
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add_numbers(5, 10))


# Example 3: Function with default arguments
def greet_user(name="Guest"):
    """Greets a user by name, or uses default value."""
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user()


# Example 4: Function returning multiple values
def min_max_sum(numbers):
    """Returns min, max, and sum of a list."""
    return min(numbers), max(numbers), sum(numbers)

nums = [3, 8, 2, 7]
print(min_max_sum(nums))