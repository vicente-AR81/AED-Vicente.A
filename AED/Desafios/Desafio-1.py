#Codigo de Numeros enteros equilibrados alumn:VAH

p = input("Ingrese un numero de 6 digitos: ")
Numero = int(p)

if len(p) == 6:
    Invertido = int(p[5] + p[4] + p[3] + p[2] + p[1] + p[0])

    # Numero de adelante
    Delante1 = int(p[0])
    Delante2 = int(p[1])
    Delante3 = int(p[2])
    Suma_Delante = Delante1 + Delante2 + Delante3

    # Numeros de atras
    Atras1 = int(p[3])
    Atras2 = int(p[4])
    Atras3 = int(p[5])
    Suma_Atras = Atras1 + Atras2 + Atras3

    # Diferencia p - pi
    Dif = abs(Numero - Invertido)
    Dif = str(Dif)
    Dif = str(Dif).zfill(6)
    Dif_Delante1 = int(Dif[0])
    Dif_Delante2 = int(Dif[1])
    Dif_Delante3 = int(Dif[2])
    Dif_Atras1 = int(Dif[3])
    Dif_Atras2 = int(Dif[4])
    Dif_Atras3 = int(Dif[5])
    Dif_Delante = Dif_Delante1 + Dif_Delante2 + Dif_Delante3
    Dif_Atras = Dif_Atras1 + Dif_Atras2 + Dif_Atras3

    if Suma_Delante == Suma_Atras:
        print("Su numero es ESM")
        if Dif_Delante == Dif_Atras:
            print("Su numero es Armonico")
        else:
            print("Su numero es Balanceado")
    else:
        print("Su numero es Inestable")
else:
    print("Numero no valido para este desafio")

