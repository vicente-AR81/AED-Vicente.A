#Menu de opciones basico, con triangulo

Lado1 = int(input("Ingrese el primer lado de su triangulo: "))
Lado2 = int(input("Ingrese el segundo lado de su triangulo: "))
Lado3 = int(input("Ingrese el tercer lado de su triangulo: "))
Opcion = int(input("Ingrese 1 para calcular superficie, 2 para perimetro o 3 para lado menor: "))

s = (Lado1 + Lado2 + Lado3) / 2

if Opcion == 1:
    Superficie = (s * (s -Lado1) * (s - Lado2) * (s - Lado3)) ** 0.5
    print("La superficie de su triangulo es de: ", Superficie)

elif Opcion == 2:
    Perimetro = (Lado1 + Lado2 + Lado3)
    print("El perimetro de su triangulo es de: ", Perimetro)

elif Opcion == 3:
    if Lado1 > Lado2:
        menor = Lado2
    else:
        menor = Lado1

    if Lado3 < menor:
        menor = Lado3

    print("El lado menor de su triangulo es de: ", menor)

else:
    print("Valor invalido")