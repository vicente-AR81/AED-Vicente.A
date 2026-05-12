#Resuelto en 18 minutos, todos los resultados correctos

import random
a = 0
random.seed(2759)
m1 = m2 = m3 = 0
punto2 = prom = mayor = c = punto4 = prom4 = 0

for i in range(15000):
    numero = random.randint(1, 53000)
    a += numero
    if numero < 17000:
        m1 += 1
    if numero >= 17000 and numero < 37000:
        m2 += 1
    if numero >= 37000:
        m3 += 1

    if numero >= 25000 and numero % 4 == 0:
        punto2 += numero
        c += 1

    if numero % 3 == 0 and numero > mayor:
        mayor = numero

    if numero % 5 == 0:
        punto4 += 1

if punto2 != 0:
    prom = punto2 // c
if punto4 != 0:
    prom4 = (punto4 * 100) // 15000

print(a)
print("Cantidad de numeros menores que 17000:", m1)
print("Cantidad de numeros entre 17000 y 37000", m2)
print("Cantidad de numeros mayores que 37000", m3)
print("El promedio de numeros mayores que 25000 es:", prom)
print("El numero divisible por 3 mayor es:", mayor)
print("El promedio de numeros divisibles por 5 sobre el total es:", prom4)