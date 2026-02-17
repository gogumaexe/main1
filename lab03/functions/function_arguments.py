# function_arguments.py
# Demonstrates positional, keyword, and default arguments

def describe_person(name, age=18, country="Unknown"):
    """Displays information about a person."""
    print(f"Name: {name}, Age: {age}, Country: {country}")

# Positional arguments
describe_person("John", 25, "USA")

# Keyword arguments
describe_person(country="Canada", name="Lara", age=22)

# Using default values
describe_person("Mike")