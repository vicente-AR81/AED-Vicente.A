#Mantenimiento de PCs

#PC1
print("PC1")
Serie1 = int(input("Ingrese el numero de serie de la primer PC: "))
Tiempo1 = int(input("Ingrese el tiempo de reparacion de la PC en minutos: "))
Causa1 = int(input("Ingrese 1 si el problema fue de hardware, 2 si fue de software: "))

#PC2
print("PC2")
Serie2 = int(input("Ingrese el numero de serie de la segunda PC: "))
Tiempo2 = int(input("Ingrese el tiempo de reparacion de la PC en minutos: "))
Causa2 = int(input("Ingrese 1 si el problema fue de hardware, 2 si fue de software: "))

#PC3
print("PC3")
Serie3 = int(input("Ingrese el numero de serie de la tercer PC: "))
Tiempo3 = int(input("Ingrese el tiempo de reparacion de la PC en minutos: "))
Causa3 = int(input("Ingrese 1 si el problema fue de hardware, 2 si fue de software: "))

T_total = Tiempo1 + Tiempo2 + Tiempo3
T_Promedio = (Tiempo1 + Tiempo2 + Tiempo3) / 3
mayor = max(Tiempo1, Tiempo2, Tiempo3)

print("El tiempo total de mantenimientos fue de: ", T_total, "Minutos")
print("El tiempo promedio fue de: ", T_Promedio, "Minutos")

if mayor == Tiempo1:
    print("La PC con mayor tiempo de mantenimiento es:", Serie1)
elif mayor == Tiempo2:
    print("La PC con mayor tiempo de mantenimiento es:", Serie2)
else:
    print("La PC con mayor tiempo de mantenimiento es:", Serie3)

if Causa1 == 1 and Causa2 == 1 and Causa3 == 1:
    print("Todas las PCs tuvieron problemas de Hardaware")