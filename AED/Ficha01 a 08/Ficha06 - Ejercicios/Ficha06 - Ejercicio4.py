import random
i = 0
p = 0
s = 0

while i < 1000:
    n = random.randint(0, 100000)
    s += n
    i += 1

p = s / i

print("Su promedio es de:", p)