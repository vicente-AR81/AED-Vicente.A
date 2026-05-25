n = int(input("Ingrese la cantidad de ciclistas: "))
Record = int(input("Ingrese el record de la carrera: "))
i = 0
t_total = 0
competidores = []
tiempos = []

for i in range(n):
    c = input("Ingrese el nombre del ciclista: ")
    t = int(input("Ingrese el tiempo del ciclista: "))

    competidores.append(c)
    tiempos.append(t)
    t_total = t_total + t
    i += 1

t_ganador = max(tiempos)
gandor = tiempos[tiempos.index(t_ganador)]
ganador = competidores[competidores.index(gandor)]

promedio = t_total / n

if Record > t_ganador:
    print("El nuevo record es de: ", t_ganador)

