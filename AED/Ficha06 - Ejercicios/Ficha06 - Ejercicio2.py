v = int(input("Ingrese la venta: "))
cantidad = 0
total = 0
c = 0
d = 0
e = 0

while v >= 0:

    if 100 <= v <= 300:
        c += 1
    if v == 400 or v == 500 or v == 600:
        d += 1
    if v < 50:
        e += 1

    cantidad += 1
    total += v
    v = int(input("Ingrese la venta: "))

print("Cantidad de ventas:", cantidad)
print("Total de ventas:", total)
print("Ventas entre 100 y 300:", c)
print("Ventas de 400, 500 o 600:", d)
if e > 0:
    print("Hubo ventas menores a 50")
else:
    print("No hubo ventas menores a 50")