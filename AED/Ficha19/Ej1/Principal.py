from Clase import *

def cargar(v):
    n = 2
    for i in range(n):
        v[i] = Punto(int(input("Ingrese el valor del punto en x: ")), int(input("Ingrese el valor del punto en y: ")))

    for j in range(n):
        print("Punto:", j + 1 ,"Posiciones:", v[j])


def cuadrantes(v):
    for i in range(len(v)):
        if v[i].x > 0 and v[i].y > 0:
            print("Punto:", i + 1 ,"Cuadrante: 1")
        elif v[i].x < 0 and v[i].y > 0:
            print("Punto:", i + 1 ,"Cuadrante: 2")
        elif v[i].x < 0 and v[i].y < 0:
            print("Punto:", i + 1 ,"Cuadrante: 3")
        else:
            print("Punto:", i + 1 ,"Cuadrante: 4")


def iguales(v):
    for i in range(len(v) - 1):
        if v[i].x > 0 and v[i+1].x > 0:
            if v[i].y > 0 and v[i+1].y > 0:
                print("Estan en el mismo cuadrante")
            elif v[i].y < 0 and v[i+1].y < 0:
                print("Estan en el mismo cuadrante")
            else:
                print("NO estan en el mismo cuadrante")
        elif v[i].x < 0 and v[i + 1].x < 0:
            if v[i].y > 0 and v[i+1].y > 0:
                print("Estan en el mismo cuadrante")
            elif v[i].y < 0 and v[i+1].y < 0:
                print("Estan en el mismo cuadrante")
            else:
                print("NO estan en el mismo cuadrante")
        else:
            print("NO estan en el mismo cuadrante")


def principal():
    vector = 2 * [0]
    cargar(vector)
    cuadrantes(vector)
    iguales(vector)

if __name__ == "__main__":
    principal()
