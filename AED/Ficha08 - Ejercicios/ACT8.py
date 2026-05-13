#Simulacro todo correcto

import random
random.seed(95)
n = 45000
c1 = 0
div6 = div9 = ambos = 0
mayor = 0
segundo = 95001
prom = 0
for i in range(n):
    num = random.randint(1,95000)
    if i == 1:
        segundo = num

    if num < segundo:
        c1 += 1

    if num % 6 == 0:
        div6 += 1
    if num % 9 == 0:
        div9 += 1
    if num % 6 == 0 and num % 9 == 0:
        ambos += 1

    if num % 4 == 0 and num > mayor:
        mayor = num

if c1 != 0:
    prom = (c1 * 100) // n

print(c1)
print(div6)
print(div9)
print(ambos)
print(mayor)
print(prom)