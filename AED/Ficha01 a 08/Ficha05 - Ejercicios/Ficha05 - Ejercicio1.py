#Operacion de orden con 3 numeros

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a > b:
    menor, mayor = b, a
else:
    menor, mayor = a, b

if c > mayor:
    medio, mayor = mayor, c
else:
    if c > menor:
        medio = c
    else:
        medio, menor = menor, c

print("El numero mayor es:", mayor)
print("El numero del medios es:", medio)
print("El numero menor es:", menor)

# 3 es resto de div de los 2 primeros
if mayor % medio == menor:
    print("La division entre los dos primeros da de resto el menor numero")
else:
    print("La division entre los dos primeros NO da de resto el menor numero")