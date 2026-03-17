print(isinstance(5, int))  # True
x = str(10)
print(x)

for idx, value in enumerate(['a', 'b', 'c']):
    print(idx, value)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)