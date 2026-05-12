import random
random.seed(3374)
n = 19000
suma = 0
c1 = c2 = c3 = 0
p2 = cont2 = prom = 0
menor = 15000
p4 = prom2 = 0

for i in range(n):
    num = random.randint(-1000, 15000)
    suma += num

    #Punto 1
    if num < 0:
        c1 += 1
    if 0 <= num < 12000 and num % 5 == 0:
        c2 += 1
    if num >= 12000 and num % 3 == 0:
        c3 += num

    #Punto 2
    if -200 <= num <= 3000:
        p2 += num
        cont2 += 1

    #Punto 3
    if num > 0 and num % 9 == 0:
        if menor > num:
            menor = num

    #Punto 4
    if num < 0 and num % 2 == 0:
        p4 += 1


if cont2 > 0:
    prom = p2 // cont2
if p4 > 0:
    prom2 = (p4 * 100)// n

print(suma)
print(c1)
print(c2)
print(c3)
print(prom)
print(menor)
print(prom2)