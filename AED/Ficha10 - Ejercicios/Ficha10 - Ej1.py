cadena = input("Ingrese su texto a analizar: ")

cp4 = 0
cpxy = 0
cletras = 0
aletras = 0
palabras = 0
xy = 0
sm = False
smo = False
mo = 0
cmo = 0

for car in cadena:
    if car == ' ' or car == '.':
        if cletras > 0:
            aletras += cletras
            palabras += 1
            if cletras > 4:
                cp4 += 1
            if cpxy != 0:
                xy += 1
            if cmo == 1:
                mo += 1

        cletras = 0
        cpxy = 0
        smo = False
        sm = False
        continue

    cletras += 1

    if car.lower() == 'x' or car.lower() == 'y':
        cpxy += 1

    if car.lower() == 'm':
        sm = True
    else:
        if car.lower() == 'o' and sm:
            cmo += 1
            smo = False
        sm = False

prom = aletras / palabras
print(cp4)
print(xy)
print(prom)
print(mo)