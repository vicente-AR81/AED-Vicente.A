#Correcto desarrollo del programa
#Mejorar velocidad

n = open("entrada.txt")
texto = n.read()

def calculo_porcentaje(a,b):
    porcentaje = 0
    if b > 0:
        porcentaje = (a * 100) // b
    return porcentaje



def principal():
    r1 = r2 = r3 = r4 = 0
    cc = 0
    digito = 0
    conso = 0
    cvocal = 0
    ultimo = ""
    palvocal = 0
    palabras = 0
    fd = False
    fde = False
    cont4 = 0
    Vocal1 = Vocal2 = Vocal3 = False
    for car in texto:
        if car in " .":
            if digito != 0 and conso >= 2:
                r1 += 1

            if cvocal != 0 and ultimo in "1234567890":
                palvocal +=1

            if Vocal1 and Vocal2 and Vocal3:
                r3 += 1

            if cont4 != 0:
                r4 += 1

            Vocal1 = Vocal2 = Vocal3 = False
            palabras += 1
            conso = digito = cc = 0
            cvocal = 0
            cont4 = 0
            fd = False
            fde = False
        else:

            cc += 1
            if (cc == 2 or cc == 3) and car in "1234567890":
                digito += 1
            if cc > 3 and car.lower() not in "aeiouáéíóú1234567890":
                conso += 1
            if car in "aeiouAEIOUÁÉÍÓÚáéíóú":
                cvocal += 1

            if cc == 1 and car in "aeiouAEIOUÁÉÍÓÚáéíóú":
                Vocal1 = True
            if cc == 2 and car in "aeiouAEIOUÁÉÍÓÚáéíóú":
                Vocal2 = True
            if cc == 3 and car in "aeiouAEIOUÁÉÍÓÚáéíóú":
                Vocal3 = True

            if car in "Dd":
                fd = True
            else:
                if fd and car in "EéÉe":
                    fde = True
                fd = False

            if fde and car in "Tt":
                cont4 += 1
            ultimo = car


    r2 = calculo_porcentaje(palvocal, palabras)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == "__main__":
    principal()