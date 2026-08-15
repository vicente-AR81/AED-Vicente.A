abrir = open("entrada.txt")
texto = abrir.read()

def calculo_porcentaje(a,b):
    porcentaje = 0
    if b > 0:
        porcentaje = (a * 100) // b
    return porcentaje



def principal():
    r1 = r2 = r3 = r4 = 0
    ccaracteres = 0
    cvocal = 0
    for car in texto:
        print(car)
        if car in " .":
            #El continue si o si va

            #En esta parte de aca vas a calcular los diferentes resultados
            #En este caso r1, r2, r3, r4 que son los que te piden los enunciados

            #aca reinicias contadores en este caso el contador de caracteres
            ccaracteres = 0
            cvocal = 0
            continue
        else:
            ccaracteres += 1

            #Aca vas a hacer las diferentes preguntas que te pida el enunciado
            #Por ejemplo verficar si la palabra tiene vocal
            if car in "aeiouAEIOUÁÉÍÓÚáéíóú":
                cvocal += 1


            pass

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == "__main__":
    principal()