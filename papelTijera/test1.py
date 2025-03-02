
import random 
from random import randint 

num =[]
for x in range(0,10):
    num.append(randint(1,10))
    
print(num)    

numbs = random.sample(range(0,10),10)
print(numbs)




import random

def parsea_jugada_usuario(eleccion_usuario:int)->int:
    ''' 
    Comprueba que el usuario haya elegido 0,1 o 2 (piedra, papel o tijeras) y devuelve la elección. Si la elección no es válida, devuelve -1.     
    '''
    if eleccion_usuario not in [0,1,2]:
        # Valor no válido
        eleccion_usuario = -1
    return eleccion_usuario

def get_jugada_ordenador()->int:
    ''' 
    Elige aleatoriamente entre piedra (0), papel(1) o tijeras(2) y devuelve la elección.     
    '''
    res = random.randint(0, 2)
    return res

def determina_ganador(jugada_usuario:int, jugada_ordenador:int)->int:
    ''' Determina el ganador del juego en base a la selección 
    realizada por el usuario y el ordenador. 
    0: empate, 1: gana usuario, -1: gana ordenador . '''
    if jugada_usuario == jugada_ordenador:
        resultado = 1
    elif jugada_usuario == 0 and jugada_ordenador == 2:
        resultado = 1
    elif jugada_usuario == 2 and jugada_ordenador == 1:
        resultado = 1
    elif jugada_usuario == 1 and jugada_ordenador == 0:
        resultado = 1
    else:
        resultado = -1
    
    return resultado

def jugar_una(eleccion_usuario:int)->tuple[int, int]:
    '''
    Función principal que ejecuta el juego de Piedra, Papel o Tijeras.
    '''
    eleccion_ordenador = get_jugada_ordenador()
    eleccion_usuario_1 = parsea_jugada_usuario(eleccion_usuario)    
    resultado = determina_ganador(eleccion_usuario_1, eleccion_ordenador)
    return eleccion_ordenador, resultado

import random

def parsea_jugada_usuario(eleccion_usuario:int) -> int:
    if eleccion_usuario not in [0,1,2]:
        eleccion_usuario = -1
    return eleccion_usuario

def get_jugada_ordenador() -> int:
    res = random.randint(0,2)
    return res

def determina_ganador(jugada_usuario:int, jugada_ordenador:int) -> int:
    if jugada_usuario == 0 and jugada_ordenador == 2:
        resultado = 1
    elif jugada_usuario == 2 and jugada_ordenador == 1:
        resultado = 1
    elif jugada_usuario == jugada_ordenador:
        resultado = 0
    elif jugada_usuario == 1 and jugada_ordenador == 0:
        resultado = 1
    else:
        resultado = -1
    return resultado

''' 
def jugar_mejor_de_n(n:int)->None:
    puntos_usuario = 0
    puntos_computadora = 0
    while puntos_usuario<n and puntos_computadora<n:
        eleccion_ord, result = jugar_partida()
        print(f"El ordenador eligió: {OPCIONES[eleccion_ord]}")
        print(f"Resultado: {RESULTADO[result]}")
        if result == 1:
            puntos_usuario += 1
        elif result == -1:
            puntos_computadora += 1
        else:
            result += 0
    return puntos_usuario, puntos_computadora



def main()->None:
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    #eleccion_ord, result = jugar_partida()
    #print(f"El ordenador eligió: {OPCIONES[eleccion_ord]}")
    #print(f"Resultado: {RESULTADO[result]}")
    usuario, ordenador = jugar_mejor_de_n(3)
    if usuario>ordenador:
        print("¡Felicidades! Has ganado la partida: ", usuario, " a ", ordenador)
    else:
        print("Lo siento has perdido: ", usuario, " a ", ordenador)



if __name__ == "__main__":
    main()
    
    '''