#Se necesita desarrollar un programa que permita calcular
# la suma de tres números. Si el resultado es mayor a 10
# dividir por 2 (mostrar su resultado sin decimales),
# en caso contrario elevar el resultado al cubo.

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

suma = a + b + c

if suma > 10:
    suma = suma // 2
else:
    suma = suma ** 3

print("Su resultado es: ", suma)