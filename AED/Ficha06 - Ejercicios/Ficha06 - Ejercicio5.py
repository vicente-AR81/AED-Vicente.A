import random
x = 0
mayor = -100000
a = 0

while x < 10000:
    n = random.randint(-100000, 100000)
    x += 1
    if n > mayor:
        mayor = n
    if n > 0:
        a += 1

if a != 0:
    p = round((a / x) * 100, 2)
else:
    p = 0
print("Su promedio es de positivos sobre numeros generados es de:", p)
print("El numero mayor es:", mayor)