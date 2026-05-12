n = int(input("Ingrese un la cantidad de numeros que quiere transformar: "))
num = int(input("Ingrese su primer numero: "))
mayor = num
segmayor = num
mayorneg = None
a = c = 0
for i in range(n-1):
    if mayor < num:
        segmayor = mayor
        mayor = num
    if num < 0 :
        mayorneg = num

    if num > 0:
        a += num
        c += 1

    num = int(input("Ingrese otros numeros: "))

if a != 0:
    prom = (a / c)
else:
    prom = 0

print("El promedio de positivos es de: ", prom)
print("El segundo numero mayor es: ", segmayor)
print("Mayor negativo es: ", mayorneg)
