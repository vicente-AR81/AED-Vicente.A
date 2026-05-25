#Temperaturas

Temp1 = int(input("Ingrese el valor de la primer temperatura: "))
Temp2 = int(input("Ingrese el valor de la segunda temperatura: "))
Temp3 = int(input("Ingrese el valor de la tercera temperatura: "))
Temp4 = int(input("Ingrese el valor de la cuarta temperatura: "))

Prom = (Temp1 + Temp2 + Temp3 + Temp4) / 4

Temp_Max = max(Temp1, Temp2, Temp3, Temp4)
Temp_Min = min(Temp1, Temp2, Temp3, Temp4)

print("La temperatura promedio fue de: ", Prom)
print("La temperatura maxima fue de: ", Temp_Max)
print("La temperatura minima fue de: ", Temp_Min)

if Temp1 > Prom or Temp2 > Prom or Temp3 > Prom or Temp4 > Prom:
    print("Al menos una de las temperaturas es mayor al promedio")
