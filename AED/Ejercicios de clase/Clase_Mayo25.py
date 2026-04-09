#Calculo de raices vascara

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

Determinante = ((b**2) - 4*a*c)

if Determinante >= 0:
    x1 = (-b + (Determinante ** (1/2))) / (2*a)
    x2 = (-b - (Determinante ** (1/2))) / (2*a)
    print("El valor de la raíz 1 es:", x1)
    print("El valor de la raiz 2 es:", x2)
else:
    real = -b / (2 * a)
    imaginaria = ((-Determinante) ** 0.5) / (2 * a)
    print("El valor de la raíz 1 es:", real, "+", imaginaria, "i")
    print("El valor de la raíz 2 es:", real, "-", imaginaria, "i")