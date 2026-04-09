#Eleccion presidencial

#Partido 1
Presidente_1 = input("Ingrese el nombre completo del candidato a presidente: ")
Vice_1 = input("Ingrese el nombre completo del candidato a vicepresidente: ")
Votos_1 = int(input("Ingrese la cantidad de votos del partido: "))
Partido_1 = Presidente_1, Vice_1, Votos_1

#Partido 2
Presidente_2 = input("Ingrese el nombre completo del candidato a presidente: ")
Vice_2 = input("Ingrese el nombre completo del candidato a vicepresidente: ")
Votos_2 = int(input("Ingrese la cantidad de votos del partido: "))
Partido_2 = Presidente_2, Vice_2, Votos_2

#Partido 3
Presidente_3 = input("Ingrese el nombre completo del candidato a presidente: ")
Vice_3 = input("Ingrese el nombre completo del candidato a vicepresidente: ")
Votos_3 = int(input("Ingrese la cantidad de votos del partido: "))
Partido_3 = Presidente_3, Vice_3, Votos_3

Votos_Totales = Votos_1 + Votos_2 + Votos_3

Porcentaje_1 = (Votos_1 / Votos_Totales) * 100
Porcentaje_2 = (Votos_2 / Votos_Totales) * 100
Porcentaje_3 = (Votos_3 / Votos_Totales) * 100

#Ordenamos de mas porcentaje a menos
if Porcentaje_1 > Porcentaje_2:
    mayor, menor = Porcentaje_1, Porcentaje_2
    primero, ultimo = Partido_1, Partido_2
else:
    mayor, menor = Porcentaje_2, Porcentaje_1
    primero, ultimo = Partido_2, Partido_1

if Porcentaje_3 > mayor:
     medio, mayor = mayor,Porcentaje_3
     segundo, primero = primero, Partido_3
else:
    if Porcentaje_3 > menor:
        medio = Porcentaje_3
        segundo = Partido_3
    else:
        medio, menor = menor, Porcentaje_3
        segundo, ultimo = ultimo, Partido_3

#Una vez ordenados podemos comparar con el articulo 149

if mayor > 45:
    print("El partido ganador es el: ", primero)
elif mayor > 40 and mayor - medio > 10:
    print("El partido ganador es el: ", primero)
else:
    print("Se requiere segunda vuelta y participan los partidos: ", primero, segundo)