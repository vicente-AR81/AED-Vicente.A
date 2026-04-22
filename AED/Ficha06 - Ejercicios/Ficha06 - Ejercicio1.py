#gestor de cine
c = int(input("Ingrese la cantidad de funciones: "))
c1 = c
recaudacion = 0
fd = 0

while c > 0:
    s = int(input("Ingrese el numero de espectadores: "))
    n = int(input("Ingrese el porcentaje de descuento: "))

    if n == 0:
        precio = 75
    else:
        precio = 50
        fd += 1

    while s > 0:
        recaudacion += precio
        n -=1

    c-= 1

total_descuentos = round((fd / c1) * 100, 2)

print("Total recaudado:", recaudacion, "$")
print("Funciones con descuento:", fd)
print("Porcentaje de funciones con descuento:", total_descuentos, "%")


