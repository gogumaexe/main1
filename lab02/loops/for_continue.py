for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

numbers = [4, -2, 7, -1, 9]
for n in numbers:
    if n < 0:
        continue
    print(n)

text = "p y t h o n"
for ch in text:
    if ch == " ":
        continue
    print(ch)

numbers = [1, 0, 2, 0, 3]
for n in numbers:
    if n == 0:
        continue
    print(n)