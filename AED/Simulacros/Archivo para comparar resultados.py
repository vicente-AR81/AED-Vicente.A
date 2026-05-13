import random

# Problema P1T4 - Parcial 1 - Tema 4
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(7658)

# cantidad fija de números a procesar...
n = 25000

# variable para contener al mayor pedido...
may = None

# inicialización de contadores, acumuladores y otras variables necesarias...
c1, c2, c3, a, c, ci = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(-2500, 45000)
    st += num

    # 1. contar cada número en los intervalos pedidos...
    if num <= -500:
        c1 += 1
    elif -500 < num < 27000:
        c2 += 1
    elif num >= 27000 and num % 10 == 0:
        c3 += 1

    # 2. sumar y contar los números positivos divisbles por 7 u 8 para el promedio pedido...
    if num > 0 and (num % 7 == 0 or num % 8 == 0):
        a += num
        c += 1

    # 3. determinar el mayor entre los negativos divisibles por 4...
    if num < 0 and num % 4 == 0:
        if may is None:
            may = num
        elif num > may:
            may = num

    # 4. contar los menores a 5000 para el porcentaje pedido...
    if num < 5000:
        ci += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números menores o iguales que -500:', c1)
print('\tCantidad de números en (-500, 27000):', c2)
print('\tCantidad de números mayores o iguales que 27000 y divisibles por 10 :', c3)
print()

print('Punto 2...')
prom = 0
if c != 0:
    prom = a // c
print('\tPromedio entero de los números positivos y divisibles por 7 o por 8:', prom)
print()

print('Punto 3...')
print('\tEl mayor de todos los números generados que sean negativos y divisibles por 4:', may)
print()

print('Punto 4...')
porc = ci * 100 // n
print('\tPorcentaje (entero) que los números menores a 5000 representan en el total:', porc, '\b%')
print()
