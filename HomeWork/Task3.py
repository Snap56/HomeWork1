# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).


x = int(input('Введите координату x : '))
y = int(input('Введите координату y : '))

if x == 0 or y == 0 :
    print('Не входит в четверть')
elif x > 0 and y > 0:
    print('Точка лежит в 1 четверти')
elif x > 0 and y < 0 :
    print('Точка лежит в 4 четверти')
elif x < 0 and y > 0:
    print('Точка лежит в 2 четверти')
elif x < 0 and y < 0:
    print('Точка лежит в 3 четверти')