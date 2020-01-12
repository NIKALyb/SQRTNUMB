import random
n1 = int(input("Введите первое число "))
n2 = int(input("Введите второе число "))
if n1 < n2:
    n3 = n2
    n2 = n1
    n1 = n3
print(random.randint(n1,n2))
