#Numeros random y menu
import random

print("1 para Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]")
print("2 para Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000]")
print("3 para Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000")

menu = int(input("Introduce un numero del 1 al 3: "))
i = 0
a = 0
m = 0
menor = 100000
mayor = 0

if menu == 1:
    while i < 1000:
        numeros = random.randint(0,100000)
        i += 1
        a += numeros

    prom = a / i
    print("El promedio de sus 1000 numeros es:", prom)

elif menu == 2:
    while i < 10000:
        numeros = random.randint(0,100000)
        i += 1

        if numeros > mayor:
            mayor = numeros
    print("El numero mayor es:", mayor)

elif menu == 3:
    while i < 5000:
        numeros = random.randint(0, 100000)
        i += 1

        if numeros < m:
            menor = numeros

        if numeros < 10000:
            a += numeros
            m += 1

    if m != 0:
        prom = a / m
    else:
        prom = 0
    print("El promedio de los numeros menores a 10000 es de: ", prom)
    print("El menor es: ", menor)
else:
    print("Numero invalido")