Semestre = 6
salario = int(input ("Ingrese el primer salario de su trabajador: "))
menor = salario
a = salario
mayor = salario
c = 0

for i in range (0, Semestre - 1):
    if salario < menor:
        menor = salario
        c = i

    if salario > mayor:
        mayor = salario

    salario = int(input("Ingrese el otro salario salario de su trabajador: "))
    a += salario
if a != 0:
    promedio = a / Semestre
else:
    promedio = 0

agui = round(mayor / 2, 2)
c += 1

print("El sueldo promedio es: $", promedio)
print("El sueldo menor es de: $", menor)
print("El aguinaldo es de: $", agui)
print("El mes del menor sueldo es:", c)