import random

def cargar_legajos(vector):
    n = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(n):
        vector.append(random.randint(100, 400))

def ordenar(vector):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]

def buscar(vector):
    Flag = 0
    n = int(input("Ingrese su legajo: "))
    for i in range(len(vector)):
        if vector[i] == n:
            Flag += 1

    return Flag


def principal():
    vector = []
    cargar_legajos(vector)
    print(vector)
    ordenar(vector)
    print("Vector ordenado: ")
    print(vector)
    valor = buscar(vector)
    if valor != 0:
        print("Legajo encontrado")
    else:
        print("Legajo No encontrado")


if __name__ == "__main__":
    principal()