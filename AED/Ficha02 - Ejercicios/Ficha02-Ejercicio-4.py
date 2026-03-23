#Polinomio de segundo grado

a = int(input("Ingrese el valor de a de su polinomio: "))
b = int(input("Ingrese el valor de b de su polinomio: "))
c = int(input("Ingrese el valor de c de su polinomio: "))
x = int(input("Ingrese el valor de x de su polinomio: "))

Pol = (a * (x**2)) + (b * x) + c
Dis = (b**2) - (4 * a * c)

print("El vaalor de su polinomio en x es igual a: ",Pol)
print("El valor del discriminante de su polinomio es igual a: ",Dis)