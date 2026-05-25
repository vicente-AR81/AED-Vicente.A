#fecha a cadena

Fecha = (input("Ingrese su fecha utilizando dd/mm/aaaa (Utilizando Ceros): "))

Dia = Fecha[0]+Fecha[1]
Mes = Fecha[3]+Fecha[4]
Year = Fecha[6]+Fecha[7]+Fecha[8]+Fecha[9]

print("Dia:", Dia, "Mes", Mes, "Año:", Year)