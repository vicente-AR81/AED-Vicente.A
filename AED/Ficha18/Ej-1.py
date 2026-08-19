import random

def cargar(est, ida, vue):
    for i in range(len(est)):
        ida[i] = random.randint(0, 20)
        vue[i] = random.randint(0, 20)

def mostrar(est, ida, vue):
    for i in range(len(est)):
        print("Estacion:", est[i], "pasajeros ida:", ida[i], "pasajeros vuelta:", vue[i])

def mayor(est, ida):
    mayor = pos = 0
    for i in range(len(est)):
        if mayor < ida[i]:
            mayor = ida[i]
            pos = i

    return pos

def no_subieron(est, vuelta):
    nosubiero = porcentaje = 0
    for i in range(len(est)):
        if vuelta[i] == 0:
            nosubiero += 1

    if nosubiero != 0:
        porcentaje = (nosubiero * 100)//len(est)

    return nosubiero, porcentaje

def ida_vuelta(est, ida, vuel):
    c = len(est) * [0]
    for i in range(len(est)):
        if ida[i] > vuel[i]:
            c[i] += 1

    for j in range(len(c)):
        if c[j] > 0:
            print("En la estacion", est[j], "hubo mas pasajeros en la ida")

def principal():
    estaciones = ["Maipú", "Borges", "Libertador", "Anchorena", "Barrancas", "San Isidro R", "Punta Chica", "Marina Nueva", "San Fernando R", "Canal", "Delta"]
    ida = len(estaciones) * [0]
    vuelta = len(estaciones) * [0]

    opcion = 0
    carga = False
    while opcion != 6:
        print("Menu de opciones:")
        print("1-Cargar")
        print("2-Mostrar")
        print("3-Mayor cantidad de pasajeros en ida")
        print("4-No subieron pasajeros en vuelta")
        print("5-Ida mayor que vuelta")
        print("6-Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            carga = True
            cargar(estaciones, ida, vuelta)
            print("Valores cargados")
            print()
        else:
            if not carga:
                print("Debe cargar datos de trenes primero")
                print()
            else:
                if opcion == 2:
                    mostrar(estaciones, ida, vuelta)
                    print()
                if opcion == 3:
                    n = mayor(estaciones, ida)
                    print("La estacion con mas pasajeros en la ida fue:", estaciones[n])
                    print()
                if opcion == 4:
                    no, porcentaje = no_subieron(estaciones, vuelta)
                    print("No subieron en:",no, "Paradas", "Porcentaje de no Subidos:", porcentaje)
                    print()
                if opcion == 5:
                    ida_vuelta(estaciones, ida, vuelta)
        if opcion == 6:
            print("Programa finalizado")


if __name__ == "__main__":
    principal()