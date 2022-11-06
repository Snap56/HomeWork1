# Вычислить число c заданной точностью d

#  Пример:


# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10


# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...



from re import X
from tkinter import N


n = int(input('Введите число d (точность вычисления): '))
d=10**(-n)
Pi=0
x=1
sign=1
print (float(d))

while True:
    a=4/x
    Pi=Pi+sign*a
    if a<d:
        break
    sign=-sign
    x=x+2
print(round(Pi,n))



