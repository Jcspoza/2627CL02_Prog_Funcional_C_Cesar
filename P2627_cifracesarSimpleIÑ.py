# Taller Programación y Robótica CMM BML – 2026 -2027 - Clase xx
# Nombre de programa :P2627_cifracesarSimpleI.py
# Tema: Programacion Funcional - Caesar Cipher
# Topicos nuevos: Criptografía y cifrados-> cifrado César + descifrado por fuerza bruta
# El find() y otros métodos de cadena : rebanado, ..
# Help() en funciones: como documentar funciones 
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 14
# https://inventwithpython.com/invent4thed/chapter14.html
# version : base por indices + añadir Ñ
# Fecha JCSP 2024 11 13
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es


ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
MAXCLAVE = len(ALFABETO)-1

# DEFINICION DE FUNCIONES
def LeoModo():
    """Lee por teclado si se quiere cifrar o descifrar
    - Sin parametros
    - Salida (string) 1 letra 'c' o 'd'
    """
    modo = ''
    while modo not in ['cifrar', 'c', 'descifrar', 'd']:
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

def CambiaMensaje(mode, menEntrada, key):
    """Cifra o descifra en mesaje de entrada y lo retorna - modo indices
    - 3 parametros:
        * mode(str): 'c' para cifrado / 'd' para descifrado
        * menEntrada(str): mensaje d eentrada
        * key(int): clave a usar en el cifrado o descifrado
    - Salida (str): mensaje de salida
    """
    if mode[0] == 'd':
        key = -key
    tSalida = ''

    for simbolo in menEntrada.upper():
        simbolIndx = ALFABETO.find(simbolo)
        if simbolIndx == -1: # Simbolo no se encontro en SIMBOLOS find da -1
            # simplemente lo añade sin cofrar o descifrar.
            tSalida += simbolo
        else: # Suma o resta la clave
            simbolIndx = simbolIndx + key
            # se podira escribir mejor symbolIndex += key
            simbolIndx = simbolIndx % len(ALFABETO)        
            # tSalida += SIMBOLOS[simbolIndx]
            tSalida = tSalida + ALFABETO[simbolIndx]
                        
    return tSalida
# FIN DE DEFINICION DE FUNCIONES

# --> El programa empieza aqui
# 0- Presentacion
print('PROGRAMA DE CIFRADO / DESCIFRADO CESAR') # 0- Presentacion
# 1- preguntar modi cifrado / descifrado
print('1-¿Quieres cifrar o descifrar?') 
Modo = LeoModo()

# 2- Pedir mensaje de entrada
MenEntrada = input('2-Escribe el mensaje a cifrar/descifrar : ')

# 3- Pedir la clave de cifrado/ descifrado
print('3-Escribe la clave Cesar de cifrado/descifrado')
Clave = LeoClave()

# 4 Fin- Cifrar o Descifrar y mostrar le texto de salida
print('-> El texto de salida es:')
MenSalida = CambiaMensaje(Modo, MenEntrada, Clave)
print(MenSalida)
