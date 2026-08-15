def longitud(cad):
    if len(cad) == 0 or len(cad) ==1:
        return len(cad)
    if cad[0] == cad[1]:
        return 1 + longitud(cad[1:])
    return 1

def contar(cad):
    if len(cad) == 0 or len(cad) ==1:
        return len(cad)
    if cad[0] != cad[1]:
        return 1 + contar(cad[1:])
    return contar(cad[1:])

def longitud_max(cad):
    if len(cad) == 0:
        return 0
    n = longitud(cad)
    max = longitud_max(cad[1:])

    if n > max:
        return n
    else:
        return max


def principal():
    n = open("copia.txt")
    cadena = n.read()

    print("La longitud del primer sector es:", longitud(cadena))
    print("La cantidad total de sectores es de:", contar(cadena))
    print("El sector con mayor longitud tiene un valor de:", longitud_max(cadena))

if __name__ == "__main__":
    principal()