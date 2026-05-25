#Resuelto con error de <= en punto 1, 10 MIN
import random
random.seed(7633)
n = 18000
suma = 0
c1 = c2 = c3 = 0
cont2 = a2 = 0
menor = 12000
cont4 = 0

for i in range(n):
    num = random.randint(500,13500)
    suma += num

    #Punto 1
    if num <= 4000:
        c1 += 1
    if 4000 < num < 10000 and num % 4 == 0:
        c2 += 1
    if num >= 10000:
        c3 += 1

    #Punto 2
    if num % 2 == 0 and num % 6 == 0:
        cont2 += 1
        a2 += num

    #Punto 3
    if num <= 12000 and num < menor:
        menor = num

    #Punto 4
    if num % 8 == 0:
        cont4 += 1

prom2 = a2 // cont2
prom4 = (cont4 * 100)// n


print(suma)
print(c1)
print(c2)
print(c3)
print(prom2)
print(menor)
print(prom4)