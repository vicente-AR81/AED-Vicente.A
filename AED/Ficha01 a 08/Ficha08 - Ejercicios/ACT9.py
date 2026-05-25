#Todo realizado correctamente

import random
random.seed(37)
n = 27000
c1 = c2 = c3 = 0
prom2 = a2 = con2 = 0
mayor = 0
cont4 = prom4 = 0

for i in range(n):
    num = random.randint(-20000, 30000)

    if num < -5000:
        c1 += 1
    if -5000 <= num < 15000:
        c2 += 1
    if num >= 15000 and num % 9 == 0:
        c3 += 1

    #Punto 2
    if num > 1000:
        numcadena = str(num)
        ultimo = int(numcadena[len(numcadena) - 1])
        if ultimo == 4 or ultimo == 6:
            con2 += 1
            a2 += num

    #Punto 3
    if num > 0 and num % 2 != 0 and num % 10 != 1:
        if mayor < num:
            mayor = num

    #Punto 4
    if num % 7 == 0:
        cont4 += 1

if con2 != 0:
    prom2 = a2 // con2

if cont4 != 0:
    prom4 = (cont4 * 100) // n

print(c1)
print(c2)
print(c3)
print(prom2)
print(mayor)
print(prom4)
