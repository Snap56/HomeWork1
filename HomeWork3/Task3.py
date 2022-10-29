# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#  Пример:


# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

list=[1.1, 1.2, 3.1, 5, 10.01]
print(list)
x=len(list)
print(x)
for i in range(x):
    list[i]=list[i]-math.floor(list[i])
    
print(list)
list.remove(0)
print(list)
max_number = round(max(list), 2)
min_number = round(min(list),2)
print(min_number)
print(max_number-min_number)



# x = 3.13
# y = x-math.floor(x)
# print(y)        
# print(round(x-int(x),4))
