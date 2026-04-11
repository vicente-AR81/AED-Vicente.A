#Gestion cursos institucion educativa

Maximo = int(input("Ingrese la cantidad maxima de alumnos por curso: "))

#Curso1
Id1 = input("Ingrese el id del curso: ")
Chicos1 = int(input("Ingrese la cantidad de chicos del curso: "))
Chicas1 = int(input("Ingrese la cantidad de chicas del curso: "))
Total1 = Chicos1 + Chicas1

#Curso2
Id2 = input("Ingrese el id del curso: ")
Chicos2 = int(input("Ingrese la cantidad de chicos del curso: "))
Chicas2 = int(input("Ingrese la cantidad de chicas del curso: "))
Total2 = Chicos2 + Chicas2

#Curso3
Id3 = input("Ingrese el id del curso: ")
Chicos3 = int(input("Ingrese la cantidad de chicos del curso: "))
Chicas3 = int(input("Ingrese la cantidad de chicas del curso: "))
Total3 = Chicos3 + Chicas3

if Total1 > Total2:
    menor = Total2
    id_menor = Id2
else:
    menor = Total1
    id_menor = Id1

if Total3 < menor:
    menor = Total3
    id_menor = Id3

print("El curso con menos alumnos es el: ", id_menor)

#% de chicos
Prom_Chicos1 = (Chicos1 * 100) / Total1
Prom_Chicos2 = (Chicos2 * 100) / Total2
Prom_Chicos3 = (Chicos3 * 100) / Total3

#% de chicas
Prom_Chicas1 = (Chicas1 * 100) / Total1
Prom_Chicas2 = (Chicas2 * 100) / Total2
Prom_Chicas3 = (Chicas3 * 100) / Total3

print("El curso", Id1, "- % chicos:", Prom_Chicos1, "- % chicas:", Prom_Chicas1)
print("El curso", Id2, "- % chicos:", Prom_Chicos2, "- % chicas:", Prom_Chicas2)
print("El curso", Id3, "- % chicos:", Prom_Chicos3, "- % chicas:", Prom_Chicas3)

#Promedio general de alumnos
Prom_Gral = (Total1 + Total2 + Total3) / 3

if Total1 > Maximo or Total2 > Maximo or Total3 > Maximo:
    print("La cantidad de estudiantes de un curso es mayor a la maxima, Abrir nuevo curso")