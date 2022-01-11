def a(n):
    if n == 0:
        return 1
    if n >= 1:
        return a(n // 2) + a(n // 3)


n = int(input('Введите число n: '))


print(a(n))


