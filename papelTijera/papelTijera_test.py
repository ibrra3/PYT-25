from papelTijera import *

OPCIONES = ["piedra", "papel", "tijeras"]
RESULTADO = ["Empatee", "Ganaste", "Perdiste"]


def empezar_juego() -> str:
    print("Cargando juego")
    player, pc = 0, 0

    for i in range(3):  # Jugar 3 rondas
        eleccion_usuario = -1  # Valor inicial fuera del rango válido

        # Solicita la entrada hasta que el usuario introduzca 0, 1 o 2
        while eleccion_usuario not in [0, 1, 2]:
            entrada = input(
                "Introduzca un valor de [0,1,2]: (0: piedra, 1: papel, 2: tijeras): "
            )
            if entrada in ["0", "1", "2"]:
                eleccion_usuario = int(entrada)
            else:
                print("Por favor, introduzca un número válido (0, 1 o 2).")

        # Procede con el juego usando la elección válida
        eleccion_ordenador, resultado, eleccion_usuario_1 = jugar(eleccion_usuario)
        if resultado == -1:
            print("Entrada inválida. Ronda omitida.")
            continue

        Rplayer, Rpc = mejor(resultado)
        player += Rplayer
        pc += Rpc

        print(f"Has elegido: {OPCIONES[eleccion_usuario_1]}")
        print(f"El ordenador eligió: {OPCIONES[eleccion_ordenador]}")
        print(f"Resultado de la ronda: {RESULTADO[resultado]}")

    winner = win(player, pc)
    return winner


def main() -> None:
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    winner = empezar_juego()
    print(f"Resultado final: {winner}")


if __name__ == "__main__":
    main()
