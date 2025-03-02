import random
from typing import Optional

OPCIONES = ["piedra", "papel", "tijeras"]
RESULTADO = ['Empate', 'Ganaste', 'Perdiste']

def parsea_jugada_usuario(eleccion_usuario: int) -> Optional[int]:
    """Comprueba que el usuario haya elegido 0, 1 o 2 (piedra, papel o tijeras).
    Devuelve la elección o None si no es válida."""
    if eleccion_usuario not in [0, 1, 2]:
        print("Valor no válido. Por favor ingrese 0 (piedra), 1 (papel) o 2 (tijeras).")
        return None
    return eleccion_usuario

def get_jugada_ordenador() -> int:
    """Genera la elección del ordenador aleatoriamente entre 0 (piedra), 1 (papel) y 2 (tijeras)."""
    return random.randint(0, 2)

def determina_ganador(jugada_usuario: int, jugada_ordenador: int) -> int:
    """Determina el ganador de la ronda: 0 para empate, 1 para victoria del usuario, 2 para victoria del ordenador."""
    if jugada_usuario == jugada_ordenador:
        return 0  # Empate
    elif (jugada_usuario, jugada_ordenador) in [(0, 2), (1, 0), (2, 1)]:
        return 1  # Usuario gana
    else:
        return 2  # Ordenador gana

def jugar(eleccion_usuario: int) -> tuple[int, int, Optional[int]]:
    """Juega una ronda y devuelve la elección del ordenador, el resultado, y la elección del usuario."""
    eleccion_ordenador = get_jugada_ordenador()
    eleccion_usuario_1 = parsea_jugada_usuario(eleccion_usuario)
    
    if eleccion_usuario_1 is None:
        return eleccion_ordenador, -1, eleccion_usuario_1
    
    res = determina_ganador(eleccion_usuario_1, eleccion_ordenador)
    return eleccion_ordenador, res, eleccion_usuario_1

def jugar_mejor_de_n(n: int) -> str:
    """Juega varias rondas hasta que uno de los jugadores gane n puntos."""
    puntos_usuario = 0
    puntos_ordenador = 0

    while puntos_usuario < n and puntos_ordenador < n:
        try:
            eleccion_usuario = int(input("Introduzca un valor de [0,1,2]: (0: piedra, 1: papel, 2: tijeras): "))
        except ValueError:
            print("Por favor, introduzca un número válido.")
            continue
        
        eleccion_ordenador, resultado, eleccion_usuario_1 = jugar(eleccion_usuario)
        
        if eleccion_usuario_1 is None:
            print("Ronda omitida debido a una entrada inválida.")
            continue
        
        print(f"Has elegido: {OPCIONES[eleccion_usuario_1]}")
        print(f"El ordenador eligió: {OPCIONES[eleccion_ordenador]}")
        print(f"Resultado de la ronda: {RESULTADO[resultado]}")

        if resultado == 1:
            puntos_usuario += 1
        elif resultado == 2:
            puntos_ordenador += 1

        print(f"Puntuación: Usuario {puntos_usuario} - Ordenador {puntos_ordenador}\n")

    if puntos_usuario > puntos_ordenador:
        return "Ganaste la partida!"
    elif puntos_ordenador > puntos_usuario:
        return "El ordenador ganó la partida."
    else:
        return "Empate final."

def main():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    resultado_final = jugar_mejor_de_n(3)
    print(resultado_final)

if __name__ == "__main__":
    main()
