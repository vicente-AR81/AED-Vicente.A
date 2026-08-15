"""
Dados n empleados de una fábrica, siendo n una variable que se ingresa por teclado,
de los cuales se conoce: el legajo, su sueldo y su antigüedad
(siendo la antigüedad un valor entre 0 y 29), se pide:
1) Ingresar los datos en tres arreglos paralelos.
2) Buscar un empleado con el legajo x, siendo x un valor que se ingresa por teclado.
   Si existe mostrar sus datos y si no mostrar un mensaje de error.
3) Ordenar el conjunto de arreglos por legajo, de menor a mayor.
4) Buscar un empleado con el legajo leg, siendo leg un valor que se ingresa por teclado.
   Si existe mostrar sus datos, y si no mostrar un mensaje de error.
5) Determinar cuántos empleados hay para cada valor posible de antiguedad (cuántos
   empleados tienen 0 años de antiguedad, cuántos tienen 1 año, y así para los 30
   valores posibles del campo antiguedad: 30 contadores).
6) Determinar el sueldo acumulado por cada valor de antiguedad posible (30 acumuladores).
"""


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n


def cargar(leg, sue, ant):
    n = len(leg)
    print("Cargue los datos de los empleados...")
    for i in range(n):
        leg[i] = int(input("Legajo: "))
        sue[i] = int(input("Sueldo: "))
        ant[i] = int(input("Antigüedad: "))
        print()


def mostrar(leg, sue, ant):
    n = len(leg)
    print("Listado de empleados:")
    for i in range(n):
        print("Legajo:", leg[i], "Sueldo:", sue[i], "Antigüedad:", ant[i])
    print()


def ordenar(leg, sue, ant):
    n = len(leg)
    for i in range(n-1):
        for j in range(i+1, n):
            if leg[i] > leg[j]:
                leg[i], leg[j] = leg[j], leg[i]
                sue[i], sue[j] = sue[j], sue[i]
                ant[i], ant[j] = ant[j], ant[i]


def contar(ant):
    n = len(ant)

    # vector de conteo...
    c = 30 * [0]

    # conteo por acceso directo...
    for i in range(n):
        p = ant[i]
        c[p] += 1

    # visualización de resultados...
    print("Conteo de frecuencias por antigüedad")
    for j in range(30):
        if c[j] != 0:
            print("Antigüedad:", j, "- Cantidad:", c[j])
    print()


def sumar(ant, sue):
    n = len(ant)

    # vector de acumulación...
    a = 30 * [0]

    # acumulación por acceso directo...
    for i in range(n):
        p = ant[i]
        a[p] += sue[i]

    # visualización de resultados...
    print("Acumulación de sueldos por antigüedad")
    for j in range(30):
        if a[j] != 0:
            print("Antigüedad:", j, "- Sueldo Acumulado:", a[j])
    print()


def secuencial(legajos, x):
    n = len(legajos)
    for i in range(n):
        if x == legajos[i]:
            return i
    return -1


def binaria(v, x):
    n = len(v)
    izq = 0
    der = n - 1
    # Mientras no se crucen
    while izq <= der:
        c = (izq + der) // 2
        if v[c] == x:
            return c
        elif v[c] > x:
            der = c - 1
        else:
            izq = c + 1
    return -1


def principal():
    print("Programa de gestión de empleados")
    n = validate(0)
    legajos = n * [0]
    sueldos = n * [0]
    antig = n * [0]

    cargar(legajos, sueldos, antig)
    mostrar(legajos, sueldos, antig)

    x = int(input("Legajo a buscar: "))
    r1 = secuencial(legajos, x)
    if r1 != -1:
        print("Encontrado:")
        print("Legajo:", legajos[r1], "Sueldo:", sueldos[r1], "Antigüedad:", antig[r1])
    else:
        print("No estaba...")
    print()

    ordenar(legajos, sueldos, antig)
    mostrar(legajos, sueldos, antig)

    x = int(input("Legajo a buscar: "))
    r1 = binaria(legajos, x)
    if r1 != -1:
        print("Encontrado:")
        print("Legajo:", legajos[r1], "Sueldo:", sueldos[r1], "Antigüedad:", antig[r1])
    else:
        print("No estaba...")
    print()

    contar(antig)
    sumar(antig, sueldos)


if __name__ == "__main__":
    principal()
