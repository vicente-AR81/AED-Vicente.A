#Calculo distancia y porcentaje

Distancia_Esperada = 3641.3
Distancia_Esperada_Mts = Distancia_Esperada * 1000
Distancia_Recorrida = int(input("Ingrese su distancia recorrida en MTS: "))

Porcentaje = (Distancia_Recorrida / Distancia_Esperada_Mts) * 100

Distancia_Km = Distancia_Recorrida // 1000
Distancia_Mts = Distancia_Recorrida % 1000

print("Recorriste un total de: ",Distancia_Km,"KM y",Distancia_Mts,"Mts lo cual representa un",Porcentaje,"%")
