#Limite de edad

Limite = int(input("Ingrese la edad limite: "))
Participante_1 = int(input("Ingrese la edad del participante: "))
Participante_2 = int(input("Ingrese la edad del participante: "))
participante_3 = int(input("Ingrese la edad del participante: "))

if Participante_1 <= Limite or Participante_2 <= Limite or Participante_3 <= Limite:
    print("La edad de alguno de los participantes es menor al limite")
else:
    print("La edad de todos los participantes es mayor al limite")