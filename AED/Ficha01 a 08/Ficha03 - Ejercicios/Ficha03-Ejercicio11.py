#Enmascarar palabra

Palabra = input("Ingrese una palabra: ")

Primer_Letra = Palabra[0]
Ultima_Letra = Palabra[len(Palabra)-1]

Oculta = Primer_Letra + ("*" * (len(Palabra ) - 2)) + Ultima_Letra

print("Su palabra oculta es: ", Oculta)
