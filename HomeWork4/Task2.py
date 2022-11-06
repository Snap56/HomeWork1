# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.






list = []
n = 76
for i in range(2,n):
    while (n % i) == 0:
                list.append(i)
                n = n / i

print("Число простое.")  if len(list)==0 else print(list)

      

    
