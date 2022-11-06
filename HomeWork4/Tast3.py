# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = []
for i in range(1,10):
    list.append(random.randrange(1,5))
print(list)
x = len(list)
list1 = []


for i in list:
  if i not in list1:
    list1.append(i)


print(list1)
