import random

from typing import Optional


def parsea_jugada_usuario(
    eleccion_usuario: int,
) -> Optional[int]:  # puede devolver none
    if eleccion_usuario not in [0, 1, 2]:
        print("Valor no válido. Por favor ingrese 0 (piedra), 1 (papel) o 2 (tijeras).")
        return None  # Devuelve un valor nulo para indicar entrada inválida
    return eleccion_usuario


def get_jugada_ordenador() -> int:
    res = random.randint(0, 2)
    return res


def determina_ganador(jugada_usuario: int, jugada_ordenador: int) -> int:
    if jugada_ordenador == jugada_usuario:
        return 0  # Empate
    elif (jugada_usuario, jugada_ordenador) in [(0, 2), (1, 0), (2, 1)]:
        return 1  # Usuario gana
    else:
        return 2  # Ordenador gana


def jugar(eleccion_usuario: int) -> tuple[int, int, Optional[int]]:
    eleccion_ordenador = get_jugada_ordenador()
    eleccion_usuario_1 = parsea_jugada_usuario(eleccion_usuario)

    if eleccion_usuario_1 is None:
        return eleccion_ordenador, -1, eleccion_usuario_1

    res = determina_ganador(eleccion_usuario_1, eleccion_ordenador)
    return eleccion_ordenador, res, eleccion_usuario_1


def mejor(resultado):
    player, pc = 0, 0
    if resultado == 1:
        player = 1
    elif resultado == 2:
        pc = 1
    return player, pc


def win(player, pc):
    if pc == player:
        return "empate final"
    elif player < pc:
        return "Gana el pc"
    else:
        return "Ganas tú"


OPCIONES = ["piedra", "papel", "tijeras"]
RESULTADO = ["Empatee", "Ganaste", "Perdiste"]
