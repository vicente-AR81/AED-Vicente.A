"""
Turno 1 Bariloche:
Desarrolle un programa completo en Python que permita generar una sucesión de 19000 números enteros aleatorios,
usando como semilla del generador al valor 4142 (es decir, random.seed(4142)). Los valores de cada uno de esos
19000 números deben estar entre -27000 y 13000 (incluidos ambos - DEBE usar random.randint(-27000, 13000) para
generar cada uno de estos números). En la última pregunta de este cuestionario, se le pedirá que suba el archivo
de código fuente: Subir el archivo de código fuente es OBLIGATORIO: no subirlo, equivale a un aplazo directo,
sin importar lo que sea que haya respondido en las preguntas previas de esta evaluación.
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:

•	Suma de todos los números generados: -132577769

A partir de esa sucesión, el programa debe:
1.	Determinar cuántos números son mayores o iguales a -27000 y menores a -13000; también determinar cuántos
    números son mayores o iguales a -13000, y cuántos números son positivos pero con su primer dígito
    igual a 3, 5 o 7.

2.	Determinar el mayor entre todos los números positivos con primer dígito par.

3.	Determinar el promedio entero entre los números mayores a 1500 pero divisibles por 3 o por 7.
    Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.

4.	Determinar el porcentaje entero que representan los números que cumplen con la condición del
    punto 3 sobre la cantidad total de números. Aclaración: NO se pide el porcentaje redondeado, sino el
    truncado, sin decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación
    que corresponda, y luego la división.

También a modo de control adicional, indicamos aquí cuáles son los resultados que debería obtener el programa si la cantidad n de números procesados fuese n = 50 en lugar de n = 19000 como se pide para entregar (Atención: estos NO SON los resultados que hay que informar. El listado es simplemente una guía para que puedan validar el programa antes de entregarlo. Lo pueden utilizar o no…)
	Suma de control para n = 50 números: -285541
	Cantidad de números en [-27000, -13000):  16
	Cantidad de números mayores o iguales a -13000:  34
	Cantidad de números positivos con primer dígito igual a 3, 5 o 7:  7
	El mayor de todos los números positivos con primer dígito par: 6666
	Promedio entero de los mayores a 1500 pero divisibles por 3 o por 7: 6139
	Porcentaje entero que los mayores a 1500 pero divisibles por 3 o por 7 representan en el total: 18
"""

import random

# inicialización de variables generales
n = 19000
s = 4142
suma = 0

# contadores, acumuladores y otras...
# ítem 1...
i1_r1 = i1_r2 = i1_r3 = 0

# ítem 2...
i2_may = None

# ítem 3...
i3_acum = i3_cont = 0

# título general...
print("Modelo de P1 - 2025")
print("Procesamiento de una secuencia")

# ajuste de semilla del generador
random.seed(s)

# ciclo de procesamiento...
for i in range(n):
    num = random.randint(-27000, 13000)
    suma += num

    # ítem 1...
    if -27000 <= num < -13000:
        i1_r1 += 1

    elif -13000 <= num:
        i1_r2 += 1

    sn = str(num)
    if num > 0 and sn[0] in "357":
        i1_r3 += 1

    # ítem 2...
    if num > 0 and sn[0] in "02468":
        if i2_may is None or num > i2_may:
            i2_may = num

    # ítem 3...
    if num > 1500 and (num % 3 == 0 or num % 7 == 0):
        i3_acum += num
        i3_cont += 1

# ítem 3: calcular el promedio pedido...
if i3_cont != 0:
    i3_prom = i3_acum // i3_cont
else:
    i3_prom = 0

# ítem 4: calcular el porcentaje pedido...
i4_porc = i3_cont * 100 // n

print("Suma de todos los números generados:", suma)
print("Cantidad de números en [-27000, -13000):", i1_r1)
print("Cantidad de números mayores o iguales a -13000:", i1_r2)
print("Cantidad de números positivos que empiezan con 3, 5, o 7:", i1_r3)
print("Mayor de los positivos que empiezan con dígito par:", i2_may)
print("Promedio de los mayores a 1500 divisibles por 3 o 7:", i3_prom)
print("Porcentaje de los mayores a 1500 divisibles por 3 o 7 sobre el total:", i4_porc)
