# Cargar por teclado el nombre de un empleado,
# su sueldo base, su código operativo (una cadena
# de la forma LLss-t donde LL son letras, ss es
# un número entre 0 y 14, y t es un número entre
# 1 y 3).
# a. Determinar si el código operativo es válido
#    o no (las letras LL deben coincidir con las
#    iniciales del nombre, ss debe estar entre 0
#    y 14, y t debe estar entre 1 y 3).
# b. Si el código es válido, calcular el sueldo
#    final, sabiendo que:
#    si t == 1, el final es igual al básico más
#       10 por ciento.
#    si t == 2, el final es igual al básico
#       menos el 2% más una suma fija de 50000
#    si t == 3, el final es igual al básico más
#       100000, pero solo si el básico es menor
#       que 900000.

nombre = input("Ingrese su nombre: ")
codigo = input("Ingrese su código: ")
base = int(input("Ingrese su sueldo base: "))

j = nombre.find(" ") + 1
ini = nombre[0] + nombre[j]

s = int(codigo[2:4])
t = int(codigo[5])

if ini == codigo[0:2] and 0 <= s <= 14 and 1 <= t <= 3:
    print("El código es correcto")

    final = 0
    if t == 1:
        final = base + (base * 0.1)

    elif t == 2:
        final = base - (base * 0.02) + 50000

    elif t == 3:
        if base < 900000:
            final = base + 100000
        else:
            final = base

    print("El sueldo final es:", final)

else:
    print("El código es incorrecto")

print("Programa terminado...")
