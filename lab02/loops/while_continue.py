i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

numbers = [3, -1, 5, -2, 7]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

i = -2
while i <= 2:
    if i == 0:
        i += 1
        continue
    print(i)
    i += 1

while True:
    x = int(input("Введите число (0 пропускаем): "))
    if x == 0:
        continue
    print("Вы ввели:", x)