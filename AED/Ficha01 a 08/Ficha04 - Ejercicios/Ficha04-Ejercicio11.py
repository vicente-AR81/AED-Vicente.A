#Galeria de arte

Cuadro_1 = int(input("Ingrese la fecha de creacion del cuadro 1: "))
Cuadro_2 = int(input("Ingrese la fecha de creacion del cuadro 2: "))
Cuadro_3 = int(input("Ingrese la fecha de creacion del cuadro 3: "))

Cuadros = [Cuadro_1, Cuadro_2, Cuadro_3]

Year_Usuario = int(input("Ingrese un año para buscar una obra: "))

if Cuadro_1 < 1901 and Cuadro_2 < 1901 and Cuadro_3 < 1901:
    print("Todos los cuadros son anteriores al siglo XX")
else:
    print("No todos los cuadros son anteriores al siglo XX")

if Year_Usuario == Cuadro_1 or Year_Usuario == Cuadro_2 or Year_Usuario == Cuadro_3:
    print("Un cuadro fue creado en la fecha que ingreso")
else:
    print("Ningun cuadro fue creado en la fecha que ingreso")

Cuadro_Nuevo = max(Cuadros)
Cuadro_Viejo = min(Cuadros)

Dif = Cuadro_Nuevo - Cuadro_Viejo

print("La diferencia entre el cuadro mas viejo y mas nuevo es de:", Dif, "años")