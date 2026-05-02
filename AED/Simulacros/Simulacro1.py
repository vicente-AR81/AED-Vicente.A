#20000 numeros
#random randit(1,45000)
import random
random.seed(49)
cont5 = cont7 = cont9 = 0
numeros = random.randint(1, 45000)
s = numeros
punto3 = 0
mayor = 0

for i in range(19999):

    if numeros % 5 == 0:
        cont5 += 1
    if numeros % 7 == 0:
        cont7 += 1
    if numeros % 9 == 0:
        cont9 += 1

    if numeros % 2 == 0 and numeros < 15000:
        punto3 += 1

    extra = str(numeros)
    pos = len(extra)
    ultimo = int(extra[pos - 1])

    if 5 <= ultimo <= 8:
        if numeros > mayor:
            mayor = numeros

    numeros = random.randint(1, 45000)
    s += numeros

if punto3 != 0:
    prom = (punto3 * 100) // 20000
else:
    prom = 0

print(s)
print(prom)
print(cont5)
print(cont7)
print(cont9)
print(punto3)
print(mayor)
