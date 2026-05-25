#Programa para calcular pago a actores

Recaudacion = float(input("Ingrese el la recaudacion de su pelicula: "))
Nombre_Actor = input("Ingrese el nombre del actor: ")
Porcentaje = float(input("Ingrese el porcentaje de salario de ese actor: "))

Porcentaje = Porcentaje/100
Salario = Recaudacion * Porcentaje

print("El salario de:", Nombre_Actor, "Es de: $", Salario)