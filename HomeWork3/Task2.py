# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:


# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

n =int (input('Введите длинну списка '))
list = []
for i in range(n):
    list.append(random.randint(0,11))
print(list)
list1 = []
# x= int(n/2 + n%2)
for a in range(int(n/2+n%2)):
        list1.append(list[a] * list[n-a-1])
print(list1)