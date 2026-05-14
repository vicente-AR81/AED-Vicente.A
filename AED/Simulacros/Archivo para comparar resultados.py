import random

# Problema P1T5 - Parcial 1 - Tema 5
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(2753)

# cantidad fija de números a procesar...
n = 30000

# variable para contener al menor pedido...
men = None

# inicialización de contadores, acumuladores y otras variables necesarias...
c1, c2, c3, a, c, ci = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(-15000, 15000)
    st += num

    # 1. contar cada número en los intervalos pedidos...
    if num < 0:
        c1 += 1
    elif 0 <= num < 5000:
        c2 += num
    elif num >= 5000 and num % 2 == 1:
        c3 += 1

    # 2. sumar y contar los números negativos divisibles por 3 y por 5 para el promedio pedido...
    if num < 0 and num % 3 == 0 and num % 5 == 0:
        a += num
        c += 1

    # 3. determinar el menor entre los negativos impares...
    if num > 0 and num % 3 == 0 and num % 4 != 0:
        if men is None:
            men = num
        elif num < men:
            men = num

    # 4. contar los números negativos impares para el porcentaje pedido...
    if num < 0 and num % 2 == 1:
        ci += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números que eran negativos:', c1)
print('\tSuma de los números mayores o iguales a cero y menores que 5000:', c2)
print('\tCantidad de números mayores o iguales que 5000 impares:', c3)
print()

print('Punto 2...')
prom = 0
if c != 0:
    prom = a // c
print('\tPromedio entero de los números generados negativos y divisibles por 3 y por 5:', prom)
print()

print('Punto 3...')
print('\tEl menor de todos los números generados mayores que cero y divisibles por 3:', men)
print()

print('Punto 4...')
porc = ci * 100 // n
print('\tPorcentaje (entero) que la cantidad de negativos impares representan en el total:', porc, '\b%')
print()
