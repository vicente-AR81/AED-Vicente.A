nmaspasos = cantpasos = 0
smayor = ""

for n in range(1111, 1112):
    pasos = 0
    secuencia = "(" + str(n) + ","
    aux = n

    while aux >= 10:
        pasos += 1
        producto = 1

        while aux > 0:
            digito = aux % 10
            producto = producto * digito
            aux = aux // 10

        secuencia += str(producto)

        if producto >= 10:
            secuencia += ","
        else:
            secuencia += ")"

        aux = producto

    #Numero con mas pasos
    if pasos > cantpasos:
        nmaspasos = n
        cantpasos = pasos
        smayor = secuencia

print("Numero con mas persistencia:", nmaspasos)
print("Persistencia de", nmaspasos, "es de:", cantpasos)
print("Secuencia de numeros para el", nmaspasos, ":", smayor)