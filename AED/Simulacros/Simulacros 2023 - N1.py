#Resuelto en 19 minutos, Todos los resultados correctos

import random
random.seed(1157)
n = 17000
suma = 0
m1 = m2 = m3 = a = x = prom = 0
menor = 37000
par = 0

for i in range(n):
    num = random.randint(1000, 37000)
    suma += num

    if num < 15000:
        m1 += 1
    if 15000 <= num < 30000:
        m2 += num
    if num >= 30000:
        m3 += 1

    if num % 7 == 0 and num % 3 != 0:
        a += num
        x += 1

    if num % 2 != 0:
        if num < menor:
            menor = num

    if num % 2 == 0:
        par += 1


if a != 0:
    prom = (a // x)

prom4 = (par * 100) // n

print(suma)
print("Cantidad de numeros menores que 15000:", m1)
print("Suma de numeros entre 15000 y 30000:", m2)
print("Cant de numeros mayores o iguales a 30000:", m3)
print("Promedio de num divisible por 7:", prom)
print("Menor impares:", menor)
print("Promedio numeros pares:", prom4)