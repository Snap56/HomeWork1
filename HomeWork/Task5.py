# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


import math
from turtle import distance


x1 = float(input('Координаты x первой точки : '))
y1 = float(input('Координаты y первой точки : '))
x2 = float(input('Координаты x второй точки : '))
y2 = float(input('Координаты y второй точки : '))

distance = round( math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)), 3)
print(distance)






















