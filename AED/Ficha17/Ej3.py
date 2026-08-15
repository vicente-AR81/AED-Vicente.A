import random

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def cargar(t,c):
    for i in range(len(t)):
        t[i] = random.randint(0,3)
        c[i] = random.randint(1,20)
        print("Articulo vendido: ", t[i], "Cantidad: ", c[i])

def sumar(t,c):
    ventas = [0, 0, 0, 0]
    for i in range(len(t)):
        tipo = t[i]
        ventas[tipo] += c[i]

    for j in range(len(ventas)):
        if ventas[j] > 0:
            print("Articulo numero", j, "vendido: ", ventas[j])
        else:
            print("Articulo numero", j, "no vendido: ", ventas[j])
        print()


def principal():
    n = validate(0)
    tipo = n * [0]
    cant = n * [0]

    cargar(tipo,cant)
    print()
    sumar(tipo,cant)



if __name__ == "__main__":
    principal()