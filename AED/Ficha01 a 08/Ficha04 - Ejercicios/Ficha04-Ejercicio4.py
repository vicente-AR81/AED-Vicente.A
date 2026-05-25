#Promedio temperaturas

Temp_1 = float(input("Ingrese la primer temperatura en C°: "))
Temp_2 = float(input("Ingrese la segunda temperatura en C°: "))
Temp_3 = float(input("Ingrese la tercer temperatura en C°: "))

Promedio = (Temp_1 + Temp_2 + Temp_3) / 3

if Temp_1 > Promedio or Temp_2 > Promedio or Temp_3 > Promedio:
    print("Existe una temperatura mayor al promedio")
else:
    print("No existe una temperatura mayor al promedio")

print("La temperatura promedio es de: ", Promedio, "C°")
