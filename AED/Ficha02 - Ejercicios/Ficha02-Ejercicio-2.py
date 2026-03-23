#Descuento de medicamentos

Descuento_Por = 0.35
Monto = int(input("Ingrese el monto de su medicamento: $"))
Descuento = Monto * Descuento_Por

Monto_Final = Monto - Descuento

print("El descuento de su medicamento es: $",Descuento)
print("El monto final de su medicamento es: $",Monto_Final)