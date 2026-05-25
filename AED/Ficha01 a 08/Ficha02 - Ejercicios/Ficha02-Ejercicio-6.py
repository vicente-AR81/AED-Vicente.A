#Recargo y descuento de pago al contado o con tarjeta

Precio_P = float(input("Ingrese el valor de su producto: $"))
Tipo_P = (input("Ingrese c si paga de contado o t si paga con tarjeta: "))

if Tipo_P == "c":
    Precio_P = Precio_P - ( Precio_P * 0.1)
    print("El precio de su producto con su forma de pago es:", Precio_P)
elif Tipo_P == "t":
    Precio_P = Precio_P + ( Precio_P * 0.05)
    print("El precio de su producto con su forma de pago es:", Precio_P)
else:
    print("Forma de pago ingresada no valida")

