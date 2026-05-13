#Resuelto en 18 Minutos #Nota 9
import random
random.seed(973)
n = 14000
suma = 0
c1 = c2 = c3 = 0
punto2 = contador = prom = 0
mayor = 0
punto4 = 0

for i in range(n):
    num = random.randint(100,21100)
    suma += num

    #Punto 1
    if num <= 11000:
        c1 += 1
    if 11000 < num < 17000 and num % 3 == 0 and num % 8 == 0:
        c2 += 1
    if num >= 17000:
        c3 += 1

    #Punto 2
    if num % 9 == 0 and num <= 15000:
        punto2 += num
        contador += 1

    if 1000 < num <= 14000:
        if mayor < num:
            mayor = num

    if num % 6 == 0:
        punto4 += 1

if contador != 0:
    prom = punto2 // contador

if punto4 != 0:
    porcentaje2 = (punto4 * 100) // n

print(suma)
print("Numeros menores o iguales que 11000:", c1)
print("Numeros entre 11000 y 17000:", c2)
print("Numeros mayores o iguales 17000:", c3)
print("Promedio:", prom)
print("Mayor:", mayor)
print("Promedio de num div por 6:", porcentaje2)