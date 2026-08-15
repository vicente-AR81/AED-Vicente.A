n = open("entrada.txt")
texto = n.read()


def principal():
    r1 = r2 = r3 = r4 = 0
    cc = cdigitos = cmayus = 0
    menor = 100
    for car in texto:
        print(car)
        if car in " .":
            if cc > 0:
                #Punto 1
                if cmayus == 0 and cdigitos == 1:
                    r1 += 1

                #Punto 2
                if cdigitos > 0 and cc < menor:
                    menor = cc

            cdigitos = cmayus = 0
            cc = 0
            continue

        else:
            cc +=1

            # Punto 1
            if car in "0123456789":
                cdigitos += 1
            if car in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                cmayus += 1

        r2 = menor

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == "__main__":
    principal()