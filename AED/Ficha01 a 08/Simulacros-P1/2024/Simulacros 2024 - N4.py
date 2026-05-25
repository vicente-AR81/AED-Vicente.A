#Todos los resultados generados excelentes
import random
random.seed(1475)

n = 17000
suma = 0
p1_c1 = p1_c2 = p1_c3 = 0
p2_c = p2_a = prom2 = 0
mayor = 5000
pares = prom4 = 0

for i in range(n):
    num = random.randint(-100, 15000)
    suma += num

    #Punto 1
    if num < 0:
        p1_c1 += num
    if 0 <= num < 10000 and num % 4 == 0:
        p1_c2 += 1
    if num >= 10000:
        p1_c3 += 1

    #Punto 2
    if 0 < num <= 8000 and num % 6 == 0:
        p2_c += 1
        p2_a += num

    #Punto 3
    if num > 5000 and num % 5 == 0:
        if num > mayor:
            mayor = num

    #Punto 4
    if num % 2 == 0:
        pares += 1

if p2_c != 0:
    prom2 = p2_a // p2_c
if pares != 0:
    prom4 = (pares * 100) // n

print(suma)
print(p1_c1)
print(p1_c2)
print(p1_c3)
print(prom2)
print(mayor)
print(prom4)