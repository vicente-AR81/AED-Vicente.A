#Cara o cruz
#Aclaracion, 1 equivale a cara y 2 A cruz
import random

Numero = random.randint(1, 2)
Usuario = input("Introduce Cara o cruz: ")

if Numero == 1 and Usuario == "cara" or Numero == 2 and Usuario == "cruz":
    print("Salio", Usuario, ", Por lo que usted gana")
else:
    print("Tuvo mala suerte, intente denuevo")

