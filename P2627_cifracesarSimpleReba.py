# Taller Programación y Robótica CMM BML – 2026 -2027 - Clase xx
# Nombre de programa :P2627_cifracesarSimpleI.py
# Tema: Progrmacion Funcional - Caesar Cipher
# Topicos nuevos: Criptografía y cifrados-> cifrado César + descifrado por fuerza bruta
# El find() y otros métodos de cadena : rebanado, ..
# Help() en funciones: como documentar funciones 
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 14
# https://inventwithpython.com/invent4thed/chapter14.html
# version : base por REBANADO
# Fecha JCSP 2024 11 13
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

version = 'BASE por REBANADO'
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAXCLAVE = len(ALFABETO)-1 # la clave de cifrado va de 0 a la longitud del alfabeto -1

# DEFINICION DE FUNCIONES
def LeoModo():
    """Lee por teclado si se quiere cifrar o descifrar
    Sin parametros
    Salida string 1 letra 'c' o 'd'
    """
    
    modosPosibles = 'cifrar', 'c', 'descifrar', 'd'
    modo = ''
    
    while modo not in modosPosibles:
        modo = input('Para cifrar escribe "cifrar" o "c" /Para descifrar "descifrar" o "d" --> ').lower()
        
    return modo[0]
            
def LeoClave():
    """Lee por teclado la clave de cifrado entre 0 y la longitud del alfabeto -1
    - Sin parametros
    - Salida (int) clave de cifrado/descifrado
    """
    
    key = -1
    while (key < 0) or (key > MAXCLAVE):
        key = int(input(f'Di la clave de cifrado/descifrado entre 0 y {MAXCLAVE} = '))
    
    return key

def CambiaMensaje(mode, mEntrada, key):
    """Cifra o descifra el mesaje de entrada y lo retorna - modo rebanar
    - 3 parametros:
        * mode(str): 'c' para cifrado / 'd' para descifrado
        * menEntrada(str): mensaje d eentrada
        * key(int): clave a usar en el cifrado o descifrado
    - Salida (str): mensaje de salida
    """
    
    ALFACIFRA = ALFABETO[key:] + ALFABETO[:key]
    print(ALFABETO)
    print(ALFACIFRA)
    tSalida = ''
    for simbolo in mEntrada.upper():
        # Paso 2.2.A SI símbolo es una letra del ALFABETO
        if simbolo in ALFABETO:
            if mode[0] == 'c':
                tSalida += ALFACIFRA[ALFABETO.find(simbolo)] # busca el indice del simbolo en alfabeto
            elif mode[0] == 'd':
                tSalida += ALFABETO[ALFACIFRA.find(simbolo)]                  
        # Paso 2.2.B: NO es letra de ALFABETO -
        else:
            # Añade a la cadena el símbolo sin cifrar ni descifrar
            tSalida += simbolo
            
    return tSalida

# El programa empieza aqui
print('PROGRAMA DE CIFRADO / DESCIFRADO CESAR')
print('Version ', version)
print('1-¿Quieres cifrar o descifrar?')
Modo = LeoModo()
MenEntrada = input('2-Escribe el mensaje a cifrar/descifrar : ')
print('3-Escribe la clave Cesar de cifrado/descifrado')
Clave = LeoClave()
print('-> El texto de salida es:')
MenSalida = CambiaMensaje(Modo, MenEntrada, Clave)
print(MenSalida)
