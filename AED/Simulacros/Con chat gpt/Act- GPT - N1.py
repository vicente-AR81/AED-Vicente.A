import random
random.seed(3344)
n = 19000
suma = 0
a = 0
for i in range(50):
    num = random.randint(-2500,45000)
    suma += num

    if num < 0:
        a += 1

print(suma)
print(a)
