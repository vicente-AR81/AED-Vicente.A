# Título general
print('Deteccion de palabras con la expresion "ta"')
print('Version 2: cargando todo el texto en una cadena...\n')

# Inicialización de flags y contadores
cl = 0  # Contador de letras en la palabra actual
ctp = 0  # Contador total de palabras
cpp = 0  # Contador de palabras que empiezan con "p"
cta = 0  # Contador de palabras que tienen la expresion "ta"

st = False  # Flag: ¿la última letra vista fue una "t"?
sta = False  # Flag: ¿se ha formado la silaba "ta" al menos una vez?

# Carga del texto completo
cadena = input('Cargue el texto completo (finalizando con un punto): ')

# Ciclo iterador para procesar el texto
for car in cadena:
    # 1. Si es un espacio o un punto, significa fin de palabra
    if car == ' ' or car == '.':
        if cl > 0:  # Si la palabra tuvo al menos una letra
            ctp += 1
            if sta:  # Si hubo 'ta' en esta palabra, la contamos
                cta += 1

        # Reiniciar contador de letras y flags para la próxima palabra
        cl = 0
        st = sta = False
        continue  # Pasa al siguiente carácter de la cadena

    # 2. Si no es fin de palabra, procesamos el carácter actual
    cl += 1

    # Detección de palabras que empiezan con "p"
    if cl == 1 and car.lower() == 'p':
        cpp += 1

    # Detección de la expresión "ta"
    if car.lower() == 't':
        st = True
    else:
        if car.lower() == 'a' and st:
            sta = True
        st = False

# Visualización de los resultados finales
print('\n--- Resultados ---')
print('1. Cantidad total de palabras:', ctp)
print('2. Cantidad de palabras que empiezan con "p":', cpp)
print('3. Cantidad de palabras con la expresion "ta":', cta)