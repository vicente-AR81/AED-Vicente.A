#Votos

Nombre = input("Ingrese el nombre del participante: ")
Apellido = input("Ingrese el apellido del participante: ")
Votos = int(input("Ingrese el numero de votos: "))

Nombre_Inicial = Nombre[0]
Apellido_Inicial = Apellido[0]
Votos_X = "x" * Votos

print("El candidato:", Nombre_Inicial,Apellido_Inicial, "Obtuvo:", Votos_X, "votos")