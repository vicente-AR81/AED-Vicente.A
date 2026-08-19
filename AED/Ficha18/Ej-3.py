import random

def cargar(c,t,im):
    n = int(input("Cuantas multas va a cargar: "))

    for i in range(n):
        c.append(random.randint(1,20))
        ultimo = str(c[i])
        ultimo = ultimo[len(ultimo)-1]
        ultimo = int(ultimo)
        if ultimo == 5 or ultimo == 0:
            t.append(0)
            im.append(1000)
        if ultimo == 1 or ultimo == 6:
            t.append(1)
            im.append(2000)
        if ultimo == 2 or ultimo == 7:
            t.append(2)
            im.append(3000)
        if ultimo == 3 or ultimo == 8:
            t.append(3)
            im.append(4000)
        if ultimo == 4 or ultimo == 9:
            t.append(4)
            im.append(5000)

def mostrar(c,t,im):
    for i in range(len(c)):
        print("Codigo: ", c[i], "Tipo de multa: ", t[i], "Importe:", im[i])

def principal():
    codigo = []
    tipo = []
    importes = []
    op = 0
    carga = False
    while op != 6:
        print("Menu")
        print("1- Cargar")
        print("2- Mostrar")
        print("6- Salir")
        op = int(input("Ingrese opcion:"))

        if op == 1:
            carga = True
            cargar(codigo, tipo, importes)
        else:
            if not carga:
                print("Cargue primero")
            else:
                if op == 2:
                    mostrar(codigo, tipo, importes)
                    print("")
        if op == 6:
            print("Programa finalizado")

if __name__ == "__main__":
    principal()