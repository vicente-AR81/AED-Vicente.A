#Calculo de salario de empleado

Horario = int(input("Ingrese 1 si su horario es diurno o 2 si es nocturno: "))
Horas = int(input("Ingrese el numero de horas de trabajo: "))
Salario = 0

if Horario == 1 or Horario == 2:
    if Horario == 1:
        Salario = Horas * 35.5
        print("Su salario es: $", Salario)
    else:
        Salario = Horas * 40.6
        print("Su salario es: $", Salario)
else:
    print("Numero de horario invalido")