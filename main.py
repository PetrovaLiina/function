x = float(input("Введите x: "))
while abs(x) <= 1:
    x = float(input('Вы ошиблись. |x| должен быть больше 1. \nВведите x: '))
n = int(input("Bведите n: "))
y = 0
for i in range(0, n, 1):
    y += 1 / ((2 * i + 1) * x ** (2 * i + 1))
y *= 2
print('Результат: ', y)
