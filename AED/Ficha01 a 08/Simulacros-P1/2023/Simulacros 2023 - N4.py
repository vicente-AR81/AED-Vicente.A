#Parcial realizado en 10 min, nota 10
import random
random.seed(7658)
n = 25000
suma = 0
c1 = c2 = c3 = 0
punto2 = cont2 = prom2 = 0
mayor = -2500
punto4 = prom4 = 0

for i in range(n):
    num = random.randint(-2500, 45000)
    suma += num

    #Punto 1
    if num <= -500:
        c1 += 1
    if -500 <= num <= 27000:
        c2 += 1
    if num >= 27000 and num % 10 == 0:
        c3 += 1

    #Punto 2
    if num >= 0 and (num % 7 == 0 or num % 8 == 0):
        punto2 += num
        cont2 += 1

    #Punto 3
    if num < 0 and num % 4 == 0:
        if num > mayor:
            mayor = num

    #Punto 4
    if num < 5000:
        punto4 += 1

if cont2 > 0:
    prom2 = punto2 // cont2

if punto4 > 0:
    prom4 = (punto4 * 100) // n

print(suma)
print(c1)
print(c2)
print(c3)
print(prom2)
print(mayor)
print(prom4)