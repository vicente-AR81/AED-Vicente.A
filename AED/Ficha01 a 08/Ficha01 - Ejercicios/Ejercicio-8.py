#Valor del perimetro de un cuadrado
#Area Base x Altura (En cuadrado ambas son iguales)

Area = int(input("Ingrese el area de su cuadrado en cm: "))

Lado = Area ** 0.5
Perimetro = Lado * 4

print("El perimetro de su cuadrado es: ",Perimetro, "Cm")