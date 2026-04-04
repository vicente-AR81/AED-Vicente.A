#Triangulo rectangulo

Lado1 = int(input("Ingrese un cateto del triangulo: "))
Lado2 = int(input("Ingrese el otro cateto del triangulo: "))

Hipotenusa = (Lado1 ** 2 + Lado2 ** 2) ** 0.5

if Lado1 > Lado2:
    print("El lado mayor vale: ", Lado1)
else :
    print("El lado mayor vale: ", Lado2)

print("La hipotenusa del triangulo vale: ", Hipotenusa)