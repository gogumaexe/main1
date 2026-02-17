# lambda_with_filter.py
# Using lambda with filter() to select data

numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Filter short words
words = ["hi", "hello", "sun", "python", "ok"]
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)