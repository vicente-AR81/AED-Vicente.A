#Cartas truco (Faltaria quitar el 8 y 9 pero es muy de exquisito)

import random

Palos = "Oro", "Basto", "Espada", "Copa"

Palo1 = random.choice(Palos)
Palo2 = random.choice(Palos)
Palo3 = random.choice(Palos)

Numero1 = random.randint(1, 12)
Numero2 = random.randint(1, 12)
Numero3 = random.randint(1, 12)

Carta1 = Numero1 , Palo1
Carta2 = Numero2 , Palo2
Carta3 = Numero3 , Palo3

print(Carta1)
print(Carta2)
print(Carta3)

if (Numero1 == 1 and Palo1 == "Espada") or (Numero2 == 1 and Palo2 == "Espada") or (Numero3 == 1 and Palo3 == "Espada"):
    print("Una de sus cartas es el ancho de espada")
else:
    print("No tiene el ancho de espada")

if Palo1 == Palo2 and Palo1 == Palo3:
    print("Sus cartas son del mismo palo")
    mayor = max(Numero1, Numero2, Numero3)
    print("Sus cartas son del mismo palo y la mayor es:", mayor, Palo1)

else:
    print("Sus cartas no son del mismo palo")

