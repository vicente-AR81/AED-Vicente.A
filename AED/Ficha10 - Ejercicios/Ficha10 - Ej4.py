from zipapp import create_archive

cadena = input("Ingrese su cadena a procesar: ")

cletras = 0
sp = False
spa = False
cpa = 0
cvocal = vocal = 0
may5 = 0

for car in cadena:
    if car == ' ' or car == '.':
        if cletras > 0:
            if spa and ultima == 'n':
                cpa += 1
            if cvocal > 2:
                vocal += 1
            if cletras > 5:
                may5 += 1
        cletras = 0
        cvocal = 0
        sp = False
        spa = False
        continue

    cletras += 1
    ultima = car

    if cletras == 1 and car.lower() == 'p':
        sp = True
    else:
        if cletras == 2 and sp and car.lower() == 'a':
            spa = True
        sp = False

    if cletras >= 3:
        if car.lower() in 'aeiou':
            cvocal += 1


print(cpa)
print(vocal)
print(may5)