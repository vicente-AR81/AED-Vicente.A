#Simulacion de dos dados

import random

Dado1 = random.randint(1,6)
Dado2 = random.randint(1,6)
Suma = Dado1 + Dado2

print("El valor del dado 1 es:", Dado1)
print("El valor del dado 2 es:", Dado2)

if Dado1 == Dado2 or Suma % 2 != 0:
    print("Gana el Jugador")
else:
    print("Gana la maquina")