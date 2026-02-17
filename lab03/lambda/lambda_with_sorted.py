# lambda_with_sorted.py
# Using lambda with sorted() for custom sorting

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30},
]

# Sort by age
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)

# Sort by name length
sorted_by_name = sorted(people, key=lambda p: len(p["name"]))
print(sorted_by_name)