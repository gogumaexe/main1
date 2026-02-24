def odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            yield i
n = int(input())
print(*odd_numbers(n))

def squares(n):
    for i in range(1, n + 1):
        yield i * i
n = int(input())
print(*squares(n))

def reverse_string(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]
s = input()
print("".join(reverse_string(s)))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = int(input())
print(*fibonacci(n))

def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i
n = int(input())
print(*divisors(n))