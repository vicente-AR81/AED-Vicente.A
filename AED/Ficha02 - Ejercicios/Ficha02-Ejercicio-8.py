#Rinde de un campo agricola
#10 m2 se obtienen 2 quintales.

Largo = float(input("Ingrese el largo de su parcela en metros: "))
Ancho = float(input("Ingrese el ancho de su parcela en metros: "))

Area = Largo * Ancho
Quintales = (Area / 10) * 2

print("El area de su parcela es:", Area, "metros cuadrados y puede producir", Quintales, "quintales de trigo" )