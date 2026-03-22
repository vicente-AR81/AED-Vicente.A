#Area de un rectangulo

Perimetro = int(input("Ingrese la longitud del perimetro en cm: "))
Lado = int(input("Ingrese la longitud de un lado en cm: "))

Lado2 = (Perimetro - (Lado * 2)) / 2

Area = Lado * Lado2

print("El area de su rectangulo es: ", Area)