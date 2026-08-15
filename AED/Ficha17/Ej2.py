import random

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def lanzar(d1, d2):
    for i in range(len(d1)):
        d1[i] = random.randint(1,6)
        d2[i] = random.randint(1,6)

    print("Resultados de dado1: ", d1)
    print("Resultados de dado2: ", d2)

def ambos(d1, d2):
    cigual = porcentaje = 0
    ctotal = len(d1)
    for i in range(len(d1)):
        if d1[i] == d2[i]:
            cigual += 1

    if ctotal != 0:
        porcentaje = (cigual * 100) // ctotal

    if porcentaje != 0:
        print("Cantidad de veces de tiradas iguales: ", porcentaje, "%")
    else:
        print("No hubo tiradas iguales")

def lan_impar(d1, d2):
    c = None
    for i in range(len(d1)):
        if (d1[i] + d2[i]) % 2 != 0 and c == None:
            c = i
    if c != None:
        print("El numero de tirada en la que la suma fue impar fue: ",c - 1)
    else:
        print("No hubo tirada con suma impar")

def mayores(d1, d2):
    mayor1 = c1 = 0
    mayor2 = c2 = 0
    for i in range(len(d1)):
        if d1[i] > mayor1:
            c1 = 0
            mayor1 = d1[i]
        if d2[i] > mayor2:
            c2 = 0
            mayor2 = d2[i]
        if d1[i] == mayor1:
            c1 += 1
        if d2[i] == mayor2:
            c2 += 1

    print("El numero mayor del dado1 fue: ", mayor1, "Frecuencia:", c1)
    print("El numero mayor del dado2 fue: ", mayor2, "Frecuencia:", c2)

def sumas_posibles(d1, d2):
    conteos = 12 * [0]
    for i in range(len(d1)):
        suma = d1[i] + d2[i]
        conteos[suma] += 1

    for j in range(len(conteos)):
        if conteos[j] != 0:
            print("Suma:", j, "- Cantidad:", conteos[j])
    print()




def principal():
    n = validate(0)
    dado1 = n * [0]
    dado2 = n * [0]

    lanzar(dado1, dado2)
    print()
    ambos(dado1, dado2)
    print()
    lan_impar(dado1, dado2)
    print()
    mayores(dado1, dado2)
    print()
    sumas_posibles(dado1, dado2)

if __name__ == "__main__":
    principal()