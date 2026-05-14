#Actividad resuelta, todos los resultados correctos
import random
random.seed(9655)

n = 21000
suma = 0
p1_c1 = p1_c2 = p1_c3 = 0
p2_a = p2_c = prom2 = 0
menor = 29000
p4_c = prom4 = 0

for i in range(n):
    num = random.randint(1000, 29000)
    suma += num

    #Punto 1
    if num < 9000:
        p1_c1 += 1
    if 9000 <= num < 19000 and num % 2 != 0 and num % 7 == 0:
        p1_c2 += 1
    if num >= 19000 and num % 3 == 0:
        p1_c3 += 1

    #Punto 2
    if 4000 <= num <= 10000:
        p2_c += 1
        p2_a += num

    #Punto 3
    if num % 5 != 0:
        if menor > num:
            menor = num

    #Punto 4
    if num >= 15000:
        p4_c += 1

if p2_c != 0:
    prom2 = p2_a // p2_c

if p4_c != 0:
    prom4 = (p4_c * 100)// n

print(suma)
print(p1_c1)
print(p1_c2)
print(p1_c3)
print(prom2)
print(menor)
print(prom4)