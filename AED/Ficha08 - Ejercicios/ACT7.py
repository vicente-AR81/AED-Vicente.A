#Actividad todo correcto
import random
random.seed(76)
n = 5000
c1 = c2 = c3 = 0
primer = 0
for i in range(n):
    num = random.randint(1, 65000)

    if i == 0:
        primer = num
    else:
        if num > primer:
            c2 += 1
    if num % 2 == 0 and num % 6 == 0:
        c1 += 1

    if 2000 <= num < 2999:
        c3 +=1

if c2 != 0:
    prom = (c2 * 100) // n

print(c1)
print(c2)
print(c3)
print(prom)
