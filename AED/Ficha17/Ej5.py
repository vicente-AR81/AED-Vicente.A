import random

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def cargar(t,d,m):
    n = validate(0)

    for i in range(n):
        t.append(random.randint(0, 9))
        d.append("Descripcion" + str(i + 1))
        m.append(random.randint(100,300))


def mostrar(t,d,m):
    for i in range(len(t)):
        print("Venta numero:", i + 1,"Tipo: ", t[i],"Descripcion:", d[i],"Monto:", m[i])

def suma(m):
    sumar = 0
    for i in range(len(m)):
        sumar += m[i]
    print("El monto total facturado: ", sumar,"$")

def tipos_ventas(t):
    contadores = 10 * [0]

    for i in range(len(t)):
        tipo = t[i]
        contadores[tipo] += 1

    for j in range(len(contadores)):
        if contadores[j] > 0:
            print("Tipo de objeto vendido:", j, "Frecuencia:", contadores[j])

def principal():
    tipos = []
    desc = []
    montos = []

    opcion = 0
    while opcion != 6:
        print("1- Cargar")
        print("2- Mostrar")
        print("3- Total")
        print("4- Listado")
        print("5- Ventas por tipo")
        print("6- Salir")
        print()
        opcion = int(input("Ingrese el numero de opcion: "))
        if opcion == 1:
            cargar(tipos, desc, montos)
        if opcion == 2:
            mostrar(tipos, desc, montos)
        if opcion == 3:
            suma(montos)
        if opcion == 5:
            tipos_ventas(tipos)
        if opcion == 6:
            break

if __name__ == "__main__":
    principal()