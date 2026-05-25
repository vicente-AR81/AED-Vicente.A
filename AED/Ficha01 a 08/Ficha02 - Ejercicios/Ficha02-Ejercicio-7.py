#Votos en congreso (Le agruego los que no votan)

Favor = int(input("Ingrese la cantidad de votos a favor: "))
Contra = int(input("Ingrese la cantidad de votos en contra: "))
Blanco = int(input("Ingrese la cantidad de votos en blanco: "))
Total = Favor + Contra + Blanco

Por_Favor = (Favor / Total) * 100
Por_Contra = (Contra / Total) * 100
Por_Blanco = (Blanco / Total) * 100

print("El porcentaje de votos a favor fue de: ",Por_Favor,"%")
print("El porcentaje de votos en contra fue de: ",Por_Contra,"%")
print("El porcentaje de votos en blanco fue de: ",Por_Blanco,"%")