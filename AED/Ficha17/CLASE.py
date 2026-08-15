import random
def generar_vector(v):
    v = []
    for i in range(7):
        v.append(random.randint(-1,10))

    return v

def mostrar_votos(vector):
    for i in range(len(vector)):
        print("Jurado", i + 1, ":", vector[i])

#Ordenar vector
def ordenar_vector(vector):
    n = len(vector)
    for i in range(n-1):
        for j in range(i + 1, n):
            if vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]

def buscar(vector, x):
    izq = 0
    der = len(vector) -1
    while izq <= der:
        c = (izq + der) // 2
        if vector[c]== x:
            return c
        elif vector[c] < x:
            der = c - 1
        else:
            izq = c +1
    return -1


def principal():
    v = []
    vector = generar_vector(v)
    mostrar_votos(vector)
    print("Ordenados")
    ordenar_vector(vector)
    mostrar_votos(vector)
    print("1ro: ", vector[0], "2do: ", vector[1], "3ro: ", vector[2] )
    dif = vector[0] - vector[-1]
    print(dif)
    x = int(input("Ingrese su puntaje a buscar: "))
    pos = buscar(vector, x)
    if pos != -1:
        print("Encontrado: ", pos)
        mayores = []
        for i in range(pos):
            mayores.append(vector[i])
        print(mayores)
    else:
        print("No encontrado")

if __name__ == "__main__":
    principal()