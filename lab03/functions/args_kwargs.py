# args_kwargs.py
# Demonstrates *args and **kwargs usage

def sum_all(*args):
    """Sums any number of arguments."""
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))


def print_user_info(**kwargs):
    """Prints user info from keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=23, country="USA")