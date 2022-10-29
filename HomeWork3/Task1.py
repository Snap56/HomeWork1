# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


n =int (input('Введите длинну списка '))
list = []
for i in range(n):
    list.append(random.randint(0,20))
print(list)
list1 = []
for i in  range(len(list)):
    if i%2 == 1:
        list1.append(list[i])
print (list1)

sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]
print(sum)
