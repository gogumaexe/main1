# map() example:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter() example:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)