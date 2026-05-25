import random
n = int(input("Ingrese la cant de numeros que quieren transformar: "))

for i in range(n):
    numero = random.randint(5000, 45000)
    hexa = hex(numero)
    print("El numero:", numero, "es:", hexa, "en hexagesimal")

