n = open("entrada.txt")
texto = n.read()

def calpromedio(a, b):
    prom = 0
    if b != 0:
        prom = a // b
    return prom



def principal():
    r1 = r2 = r3 = r4 = 0
    contcaracteres = cvocal = cdigitos = 0
    conte = contr = 0
    cont2 = a2 = 0
    primera = ""
    ultimo = ""
    for car in texto:
        print(car)
        if car in " .":

            if contcaracteres == 6 and (cvocal == 1 or cvocal == 2) and cdigitos > 0:
                r1 += 1

            if conte >= 2 and contr == 1:
                cont2 += 1
                a2 += contcaracteres

            if (ultimo in "aeiouAEIOUáéíóúÁÉÍÓÚ" and primera in "aeiouAEIOUáéíóúÁÉÍÓÚ") and (ultimo.lower() != primera.lower()):
                r3 += 1

            contcaracteres = 0
            cvocal = 0
            contr = conte = 0
            primera = ""
            ultimo = ""

            continue
        else:
            contcaracteres += 1

            if car in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                cvocal +=1
            if car in "0123456789":
                cdigitos += 1

            if car in "eEé":
                conte += 1
            if car in "Rr":
                contr += 1

            if contcaracteres == 1:
                primera = car

            ultimo = car

    r2 = calpromedio(a2, cont2)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == "__main__":
    principal()
