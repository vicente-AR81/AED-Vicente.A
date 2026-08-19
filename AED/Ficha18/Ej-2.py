import random

def cargar(dia, desc, mon):
    n = int(input("Ingrese la cantidad de transportes: "))
    for i in range(n):
        dia.append(random.randint(1, 31))
        desc.append("Descripcion" + str(i))
        mon.append(random.randint(1000, 9999))

def mostrar(dia, des, mon):
    for i in range(len(dia)):
        print("Dia:", dia[i],"Descripcion: ", des[i],"Monto:", mon[i], "$")


def promedio(dia, mon):
    a = promedio = 0
    c = len(dia)
    for i in range(c):
        a += mon[i]

    if c != 0:
        promedio = a // c
        print("Promedio de dinero reacuadodo:", promedio, "$")
    else:
        print("NO hubo viajes")

def ordenado(dia, desc, mon):
    for i in range(len(dia) - 1):
        for j in range(i + 1,len(dia)):
            if mon[i] < mon[j]:
                dia[i], dia[j] = dia[j], dia[i]
                desc[i], desc[j] = desc[j], desc[i]
                mon[i], mon[j] = mon[j], mon[i]

    for i in range(len(dia)):
        print("Dia:", dia[i],"Descripcion: ", desc[i],"Monto:", mon[i], "$")

def cantidades(dia, desc, mon):
    c = len(dia) * [0]
    for i in range(len(c)):
        c[dia[i]] +=1

    mayor = 0
    for i in range(len(c)):
        if c[i] > mayor:
            mayor = i

    print("El dia con mas viajes fue:", mayor +1)


def principal():
    dias = []
    descripcion = []
    monto = []

    carga = False
    op = 1
    while op != 6:
        print("Opciones:")
        print("1 - Cargar")
        print("2 - Mostrar")
        print("3 - Monto promedio por mes")
        print("4 - Listado ordenado")
        print("5 - Dia del mes mayor cantidad de transportes")
        print("6 - Salir")
        op = int(input("Ingrese su opcion: "))
        print()
        if op == 1:
            carga = True
            print("Datos cargados")
            cargar(dias, descripcion, monto)
            print()
        else:
            if not carga:
                print("Cargue datos primero")
            else:
                if op == 2:
                    mostrar(dias, descripcion, monto)
                elif op == 3:
                    promedio(dias, monto)
                elif op == 4:
                    ordenado(dias, descripcion, monto)
                elif op == 5:
                    cantidades(dias, descripcion, monto)
        if op == 6:
            print("Programa finalizado")


if __name__ == "__main__":
    principal()