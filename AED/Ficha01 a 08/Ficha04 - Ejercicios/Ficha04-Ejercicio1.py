#Generador de direcciones de mail

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Dominio = input("Ingrese su dominio sin el arroba: ")

Letra_Nombre = Nombre[0]
Letra_Apellido = Apellido[0]

if Letra_Nombre != Letra_Apellido:
    Mail = Letra_Nombre + Apellido + "@" + Dominio
else:
    Mail = Nombre + "." + Apellido + "@" + Dominio

print("Su mail es: ",Mail)