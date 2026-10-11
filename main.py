from basic import T,M,S, Limpiar_pantalla, escribir

BIENVENIDA = ' Bienvenido al sistema decodificador y encriptador usando el código César'

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def Decodificador():
    
    resultado=''
    
    Limpiar_pantalla()
    escribir('Bienvenido al decodificador'.upper())
    S(3)
    escribir('Tome en cuenta que el decodificador usa el alfabeto de 27 letras incluida la ñ')
    escribir('El orden es:')
    S(1)
    
    escribir('A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z')
    S(1)
    escribir('Dicho esto')
    escribir('Por favor Intrudzca el mensaje a decodificar')
    S(1)
    frase = input('> ').upper()
    
    S(2)
    escribir('Introduzca la clave por vafor')
    S(1)
    clave = int(input('> '))
    
    for letra in frase:
        if ALFABETO.find(letra) != -1:
            POSICIÓN_ACTUAL = ALFABETO.find(letra)
            NUEVA_POSICIÓN = (POSICIÓN_ACTUAL - clave) % 27
            LETRA_DECODIFICADA = ALFABETO[NUEVA_POSICIÓN]
            resultado += LETRA_DECODIFICADA
        else:
            resultado += letra
    
    Limpiar_pantalla()
    
    escribir('El mensaje dice:')
    S(2)
    escribir(f'{resultado.capitalize()}')
    
    S(3)
    escribir('Quisiera decodificar otro mensaje o volver al menú principal (1/2)')
    S(1)
    Decision_1 = input('> ')
    if Decision_1 == '1':
        Decodificador()
    elif Decision_1 == '2':
        Inicio()
    else:
        escribir('No escribió 1 o 2 se le enviará al menú principal')
        T(1.5)
        Inicio()
    
def Codificador():
    
    resultado = ''
    
    Limpiar_pantalla()
    escribir('Bienvenido al codificador'.upper())
    S(3)
    escribir('Tome en cuenta que el codificador usa el alfabeto de 27 letras incluida la ñ')
    escribir('El orden es:')
    S(3)
    
    escribir('A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z')
    escribir('Dicho esto Introdizca el mensaje a codificar')
    S(1)
    frase = input('> ').upper()
    
    S(2)
    escribir('Intriduzca la clave por favor')
    S(1)
    clave = int(input('> '))
    
    for letra in frase:
        if ALFABETO.find(letra) != -1:
            POSICIÓN_ACTUAL = ALFABETO.find(letra)
            NUEVA_POSICIÓN = (POSICIÓN_ACTUAL + clave) % 27
            LETRA_DECODIFICADA = ALFABETO[NUEVA_POSICIÓN]
            resultado += LETRA_DECODIFICADA
        else:
            resultado += letra
            
    Limpiar_pantalla()
    
    escribir('El mensaje codificado es:')
    S(2)
    escribir(f'{resultado}')
    S(1)
    escribir('La clave para decodificarlo es:')
    S(2)
    escribir(f'{clave}')
    
    (3)
    escribir('Quisiera codificar otro mensaje o volver al menú principal (1/2)')
    S(1)
    Decision_2 = input('> ')
    if Decision_2 == '1':
        Decodificador()
    elif Decision_2 == '2':
        Inicio()
    else:
        escribir('No escribió 1 o 2 se le enviará al menú principal')
        T(1.5)
        Inicio()

def Inicio():
    
    Limpiar_pantalla()
    M(BIENVENIDA)
    S(3)
    
    escribir('Estas son las opciones:')
    S(2)
    escribir('1. Codificador')
    escribir('2. Decofificador')
    escribir('3. Salir')
    S(1)
    Decision_3 = input ('> ')
    
    if Decision_3 == '1':
        Codificador()
    elif Decision_3 == '2':
        Decodificador()
    elif Decision_3 == '3':
        exit
    else:
        escribir ('No escribió ni 1 ni 2 ni 3, se reiniciará el menú')
        T(1.5)
        Inicio()
        
Inicio()