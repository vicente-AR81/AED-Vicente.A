import random

# Problema P1T3 - Parcial 1 - Tema 3
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(3374)

# cantidad fija de números a procesar...
n = 19000

# variable para contener al menor pedido...
men = None

# inicialización de contadores, acumuladores y otras variables necesarias...
r1, r2, r3, ai, ci, cpn = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(-1000, 15000)
    st += num

    # 1. contar cada número en los intervalos pedidos...
    if num < 0:
        r1 += 1
    elif 0 <= num < 12000 and num % 5 == 0:
        r2 += 1
    elif num >= 12000 and num % 3 == 0:
        r3 += num

    # 2. contar y sumar los números del intervalo [-200, 3000] para el promedio pedido...
    if -200 <= num <= 3000:
        ai += num
        ci += 1

    # 3. determinar el menor entre los no negativos divisibles por 9...
    if num >= 0 and num % 9 == 0:
        if men is None:
            men = num
        elif num < men:
            men = num

    # 4. contar los pares negativos para el porcentaje pedido...
    if num < 0 and num % 2 == 0:
        cpn += 1


# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números negativos:', r1)
print('\tCantidad de números en [0, 12000) divisibles por 5:', r2)
print('\tSuma de los números mayores o iguales a 12000 divisibles por 3:', r3)
print()

print('Punto 2...')
prom = 0
if ci != 0:
    prom = ai // ci
print('\tPromedio de los números generados que están en [-200, 3000]:', prom)
print()

print('Punto 3...')
print('\tEl menor de los números no negativos divisibles por 9:', men)
print()

print('Punto 4...')
porc = cpn * 100 // n
print('\tPorcentaje (entero) que los números pares negativos representan en el total:', porc, '\b%')
print()
