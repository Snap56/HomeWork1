# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#  Пример:


# 45 -> 101101
# 3 -> 11
# 2 -> 10


l = []
def convert(b):
    if (b == 0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b // 2)
a = int(input("Введите число: "))
convert(a)
l.reverse()
print("Двоичная форма числа:")
for i in l:
    print(i)