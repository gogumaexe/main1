# lambda_with_map.py
# Using lambda with map() to transform data

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Convert list of strings to uppercase
words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)