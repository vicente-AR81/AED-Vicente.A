cadena = input("Ingrese su cadena a procesar: ")

cletras = 0
cp3 = cp5 = cp7 = 0
puntob = pbvocales = 0
cpalabras = palabravocal = 0
vocalesc = 0
promedio = 0
sp = False
spe = 0
puntod = 0

for cad in cadena:
    if cad == ' ' or cad == '.':
        if cletras > 0:
            if cletras == 3:
                cp3 += 1
            if cletras == 5:
                cp5 += 1
            if cletras == 7:
                cp7 += 1
            if cletras > 3 and pbvocales > 0:
                puntob += 1
            if vocalesc == 1 or vocalesc == 2:
                palabravocal += 1
            if spe > 1:
                puntod += 1

        sp = False
        spe = 0
        cpalabras += 1
        vocalesc = 0
        cletras = 0
        pbvocales = 0
        continue


    cletras += 1

    if cletras == 3 and cad in 'aeiou':
        pbvocales += 1

    if cad in 'aeiou':
        vocalesc += 1

    if cad.lower() == 'p':
        sp = True
    else:
        if cad == 'e' and sp:
            spe += 1
        sp = False

if palabravocal > 0:
    promedio = (palabravocal * 100) // cpalabras

print(cp3)
print(cp5)
print(cp7)
print(puntob)
print(promedio)
print(puntod)

