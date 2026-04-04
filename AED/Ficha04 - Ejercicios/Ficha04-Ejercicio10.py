#Forma terreno y superficie

Frente = int(input("Ingrese la longitud de Frente de su terreno: "))
Fondo = int(input("Ingrese la longitud de Fondo de su terreno: "))

if Fondo == Frente:
    Area = Frente ** 2
    print("Su terreno es cuadrado y su area es de: ", Area, "Mts2")
else:
    Area = Frente * Fondo
    print("Su terreno es rectangular y su area es de: ", Area, "Mts2")