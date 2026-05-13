#Enunciado 2025 Realizado de manera correcta 10
import random
random.seed(4142)
n = 19000
suma = 0
c1 = c2 = c3 = 0
mayor = 0
a3 = cpunto3 = prom = 0

for i in range(n):
    num = random.randint(-27000,13000)
    suma += num

    #Punto 1
    if num < -13000:
        c1 += 1
    if -13000 <= num:
        c2 += 1
    if num > 0:
        numcadena = str(num)
        primer = int(numcadena[0])
        if primer == 3 or primer == 5 or primer == 7:
            c3 += 1

    #Punto 2
    if num > 0:
        numcadena = str(num)
        primer = int(numcadena[0])
        if primer % 2 == 0 and num > mayor:
            mayor = num

    #Punto 3
    if num > 1500 and (num % 3 == 0 or num % 7 == 0):
        a3 += num
        cpunto3 += 1


if cpunto3 != 0:
    prom = a3 // cpunto3

# Punto 4
prom4 = (cpunto3 * 100) // n

print(suma)
print(c1)
print(c2)
print(c3)
print(mayor)
print(prom)
print(prom4)