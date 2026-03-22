#Convertir pies a otras medidas

Pies = float(input("Ingerese su medida en Pies: "))

Pulgadas = Pies * 12
Yardas = Pies / 3
Centimetros = Pulgadas * 2.54
Metros = Centimetros / 100

print("Su medida en pies equivale a:", Pulgadas, "Pulgadas")
print("Su medida en pies equivale a:", Yardas, "Yardas")
print("Su medida en pies equivale a:", Centimetros, "Cm")
print("Su medida en pies equivale a:", Metros, "M")