#Analisis de palabra

Palabra = input("Escribi una palabra: ")

Longitud = len(Palabra)

if Palabra[Longitud - 1] == "a" or Palabra[Longitud - 1] == "e" or Palabra[Longitud - 1] == "i" or Palabra[Longitud - 1] == "o" or Palabra[Longitud - 1] == "u":
    print("Su palabra termina con una vocal")
else:
    print("Su palabra termina con una consonante")

print("La longitud de su palabra es de:", Longitud, "letras")

