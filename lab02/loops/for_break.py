for i in range(1, 10):
    if i == 5:
        break
    print(i)

numbers = [2, 4, 6, 8, 10, 7, 12]
for n in numbers:
    if n == 7:
        print("Нашли 7")
        break

word = "python"
for letter in word:
    if letter == "h":
        print("Буква h найдена")
        break
    

for _ in range(5):
    password = input("Введите пароль: ")
    if password == "admin":
        print("Вход выполнен")
        break

numbers = [3, 5, 7, -1, 9]
for n in numbers:
    if n < 0:
        print("Найдено отрицательное число")
        break