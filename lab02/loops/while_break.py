i = 1
while True:
    if i == 5:
        break
    print(i)
    i += 1

while True:
    x = int(input("Введите число больше 0: "))
    if x > 0:
        break
print("Спасибо!")

i = 1
while i <= 10:
    if i == 7:
        print("Нашли 7")
        break
    i += 1

while True:
    password = input("Пароль: ")
    if password == "admin":
        print("Вход выполнен")
        break

total = 0
while True:
    n = int(input("Введите число (0 — выход): "))
    if n == 0:
        break
    total += n
print("Сумма:", total)