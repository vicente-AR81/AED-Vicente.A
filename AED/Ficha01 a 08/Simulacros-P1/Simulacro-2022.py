#Resuelto en 21 minutos, Todos los resultados correctos

import random
random.seed(47)
n = 13000
m1 = m2 = m3 = 0
punto2 = cpunto2 = porcentaje =  0
menor = 33000

for i in range(n):
    num = random.randint(1, 33000)

    #Punto 1
    if num < 15000 and num % 4 == 0:
        m1 += 1
    if 15000 <= num < 22000 and num % 2 == 0:
        m2 += 1
    if 22000 <= num and num % 7 == 0:
        m3 += 1

    #Punto 2
    if 4000 <= num <= 11000:
        punto2 += num
        cpunto2 += 1

    #Punto 3
    if num % 100 == 23:
        if num < menor:
            menor = num

if cpunto2 != 0:
    porcentaje = (cpunto2 * 100) // n

print("Numeros menores que 15000:", m1)
print("Numeros mayores que 15000 y menores que 22000:", m2)
print("Numeros mayores que 22000:", m3)
print("La suma de numeros entre 4000 y 11000 es:", punto2)
print("Menor divisible por 23:", menor)
print("El porcentaje de numeros entre 4000 y 11000 es:", porcentaje)