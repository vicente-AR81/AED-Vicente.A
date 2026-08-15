import random

def cargar_vector(vector):
    n = 10
    for i in range(n):
        vector.append(random.randint(1,100))

def ordenar(vector):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i, n):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]


def principal():
    vector = []
    cargar_vector(vector)
    print(vector)
    ordenar(vector)
    print("Vector ordenado")
    print(vector)

if __name__ == "__main__":
    principal()