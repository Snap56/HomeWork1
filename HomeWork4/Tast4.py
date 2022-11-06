# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#  Пример:


# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import math


k = int (input ('Введите число: '))

list= []
for i in range(k+1):
    list.append(random.randint(1,100))
print(list)

s_to_file = ''


for i in range(len(list)-1):
    if list[i] !=0:
        if (k-i) == 1:
            s_to_file += str(list[i])+"x + "
        else :
            s_to_file += str(list[i])+ 'x^' + str(k-i)+ '+'

itog_to_file = s_to_file + str(list[-1])+ ' = 0'

print (itog_to_file)
file = open('file_Task4', 'a')
file.write(itog_to_file)
file.close







