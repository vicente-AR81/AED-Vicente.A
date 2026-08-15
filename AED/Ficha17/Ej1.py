import random

def cargar_temp(temp, reg, dias):
    n = int(input("Ingrese la cant de temperaturas a cargar: "))
    for i in range(n):
        temp.append(random.randint(15,30))
        reg.append(random.randint(1,20))
        dias.append(random.randint(1,30))

def ordenar(t, r, d):
    n = len(r)
    for i in range(n-1):
        for j in range(i+1, n):
            if d[i] > d[j]:
                r[j], r[i] = r[i], r[j]
                d[j], d[i] = d[i], d[j]
                t[i], t[j] = t[j], t[i]

def buscar_region(t,r,d):
    temm_region = []
    n = int(input("Ingrese la region que le interese buscar: "))
    if 0 <= n <= 20:
        for i in range(len(r)):
            if r[i] == n:
                temm_region.append(t[i])

    return temm_region

def superar(t,r,d):
    x = int(input("Ingrese la temperatura a superar: "))
    a = buscar_region(t, r, d)
    flag = False
    for i in range(len(a)):
        if a[i] > x:
            flag = True

    return flag

def sumar(t, r, d):

    n = len(r)

    a = 21 * [0]

    for i in range(n):
        p = r[i]
        a[p] += 1

    print("Acumulación de muestras por región")

    for j in range(1, 21):
        if a[j] != 0:
            print("Región:", j, "- Muestras:", a[j])

    print()


def promedio(temp):
    a = c = 0
    prom = 0
    for i in range(len(temp)):
        a += temp[i]
        c += 1
    if c!= 0:
        prom = a // c

    return prom


def principal():
    temp = []
    reg = []
    dias = []

    cargar_temp(temp, reg, dias)
    print("Temperaturas cargadas: ", temp)
    print("Regiones: ", reg)
    print("Dias: ", dias)
    print()

    ordenar(temp, reg, dias)
    print("Temperaturas cargadas: ", temp)
    print("Regiones: ", reg)
    print("Dias: ", dias)


    prom = promedio(temp)
    print("Promedio: ", prom)

    temp_region = buscar_region(temp, reg, dias)
    print("Temperaturas buscadas: ", temp_region)

    mayor = superar(temp, reg, dias)
    if mayor:
        print("La tempreatura de la region fue mayor que la ingresada")
    else:
        print("La tempreatura de la region fue menor que la ingresada")

    sumar(temp, reg, dias)

if __name__ == "__main__":
    principal()