#Parcial excelente
import random
random.seed(8665)

n = 16000
suma = 0
p1_c1 = p1_c2 = p1_c3 = 0
p2_c = p2_a = prom2 = 0
menor = 13000
c4 = prom4 = 0

for i in range(n):
    num = random.randint(-1000, 18000)
    suma += num

    #Punto 1
    if num <= 3000:
        p1_c1 += 1
    if 3000 < num < 12000:
        p1_c2 += num
    if num >= 12000 and (num % 3 != 0 and num % 4 != 0):
        p1_c3 += 1

    #Punto 2
    if num >= 0 and num % 8 == 0:
        p2_c += 1
        p2_a += num

    #Punto 3
    if 5000 <= num < 13000 and num % 2 == 0:
        if num < menor:
            menor = num

    #Punto 4
    if num > 0 and num % 2 != 0:
        c4 += 1


if p2_c != 0:
    prom2 = p2_a // p2_c

if c4 != 0:
    prom4 = (c4 * 100) // n

print(suma)
print(p1_c1)
print(p1_c2)
print(p1_c3)
print(prom2)
print(menor)
print(prom4)