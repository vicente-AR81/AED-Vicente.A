#Datos rectangulo

Largo = float(input("Ingrese el largo de su rectangulo en Centimetros: "))
Ancho = float(input("Ingrese el ancho de su rectangulo en Centimetros: "))

Perimetro = (Largo + Ancho) * 2
Area = Largo * Ancho

print("Su rectangulo tiene un perimetro de",Perimetro,"centimetros y un area de",Area,"Centimetros cuadrados")