#Simulacion de bingo
#No se como hacer los 15 numero sin que bugee
import random

Numeros = random.randint(1, 100)

Numero_1 =  int(input("Ingrese numero 1: "))
Numero_2 = int(input("Ingrese numero 2: "))
Numero_3 = int(input("Ingrese numero 3: "))

if Numero_1 == Numeros or Numero_2 == Numeros or Numero_3 == Numeros:
    print("El jugador marcó algún numero de la tarjeta")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")