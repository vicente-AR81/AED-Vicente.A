import random
n = c = a = 0
num = random.randint(0, 100000)
menor = num


if num < 10000:
    a+=num
    c += 1

while n < 4999:
    num = random.randint(0, 100000)
    if num < menor:
        menor = num
    if num < 10000:
        a += num
        c += 1
    n += 1

if c != 0:
    prom = round(a / c, 2)
else:
    prom = 0

print("El promedio es:", prom)
print("El menor es:", menor)
