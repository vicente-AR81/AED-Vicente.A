n = int(input("Ingrese cuantos puntos quiere cargar: "))
x = int(input("Ingrese la cordenada x de su punto: "))
y = int(input("Ingrese la cordenada y de su punto: "))
extra = 0
mayor = puntomayor = xmayor = ymayor = 0

for i in range(n):
    if x > 0 and y > 0:
        print("Su punto esta en el cuadrante 1")
        extra += 1
    elif x < 0 and y > 0:
        print("Su punto esta en el cuadrante 2")
    elif x < 0 and y < 0:
        print("Su punto esta en el cuadrante 3")
        extra += 1
    elif x > 0 and y < 0:
        print("Su punto esta en el cuadrante 4")
    else:
        print("Su punto esta sobre un eje y no pertenece a ningun cuadrante")

    pitagoras = ((x ** 2) + (y ** 2)) ** 0.5

    if pitagoras > mayor:
        mayor = pitagoras
        puntomayor = i + 1
        xmayor = x
        ymayor = y

    if i < n-1:
        x = int(input("Ingrese la cordenada x de su punto: "))
        y = int(input("Ingrese la cordenada y de su punto: "))


print("Puntos en cuadrante 1 o 3: ", extra)
print("El punto mas alejado del centro fue el punto numero:", puntomayor, "(",xmayor, ymayor,")")