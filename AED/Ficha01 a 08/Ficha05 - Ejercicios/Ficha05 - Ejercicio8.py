#Simulacion juegos de dardos

Record = int(input("Ingrese el puntaje record"))
Jugador1 = 0
Jugador2 = 0

print("Primera ronda")

Dardo1 = int(input("Ingrese el puntaje Dardo 1"))
Dardo2 = int(input("Ingrese el puntaje Dardo 2"))

if (Dardo1 + Dardo2) % 2 == 0:
    Jugador1 = Dardo1 + Dardo2
else:
    Jugador2 = Dardo1 + Dardo2

print("Segunda ronda")

Dardo1 = int(input("Ingrese el puntaje Dardo 1"))
Dardo2 = int(input("Ingrese el puntaje Dardo 2"))

if (Dardo1 + Dardo2) % 2 != 0:
    if Dardo1 > Dardo2:
        Jugador1 += Dardo1
        Jugador2 -= Dardo2
    else:
        Jugador1 += Dardo2
        Jugador2 -= Dardo1
else:
    if Dardo1 > Dardo2:
        Jugador2 += Dardo1
        Jugador1 -= Dardo2
    else:
        Jugador2 += Dardo2
        Jugador1 -= Dardo1

if Jugador1 == Jugador2:
    print("Los jugadores empataron")
elif Jugador1 > Jugador2:
    print("El jugador 1 gano")
elif Jugador1 < Jugador2:
    print("El jugador 2 gano")

if Jugador1 > Record and Jugador2 > Record:
    print("Ambos jugadores superaron el record")
elif Jugador1 > Record:
    print("El jugador 1 supero el record")
elif Jugador2 > Record:
    print("El jugador 2 supero el record")
else:
    print("Ningun jugador supero el record")
