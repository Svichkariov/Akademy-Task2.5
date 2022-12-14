"""
Лекция 2. Задача 2.5
Даны: три стороны треугольника.

Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""


a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))


"""
a+b>c, a+c>b, b+c>a, (a>0, b>0, c>0) - условие для проверки сторон треугольника
"""

while a <= 0  or b <= 0 or c <= 0 :
    if a <= 0:
        a = int(input('Введите первую сторону треугольника (число должно быть положительным и не равынм 0): '))
    elif b <= 0:
        b = int(input('Введите вторую сторону треугольника (число должно быть положительным и не равынм 0): '))
    else:
        c = int(input('Введите третью сторону треугольника (число должно быть положительным и не равынм 0): '))

if (a+b) > c and (a+c) > b and (b+c) > a:
    p = (a + b + c) / 2
    s = ((p * (p-a) * (p-b) * (p-c))**0.5)
    print('Площадь треугольника = ', s)
else:
    print('Вы ввели данные по которым не возможно построить треугольник')