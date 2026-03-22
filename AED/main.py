Tiempo_total = int(input("Ingrese el numero de tiempo(seg): "))

Horas = Tiempo_total // 3600
Restante = Tiempo_total % 3600
Minutos = Restante // 60
Segundos = Restante % 60

print("Tiempo: ", Horas, ":", Minutos, ":", Segundos )