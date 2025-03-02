from calificaciones import *

def solicita_notas():
    T = [1, 2, 3, 4]
    P = [1, 2]
    nombre = input("Introduzca su nombre: ")

    T[0] = float(input("Introduzca la nota del examen teórico 1: "))
    T[1] = float(input("Introduzca la nota del examen teórico 2: "))
    T[2] = float(input("Introduzca la nota del examen teórico 3: "))
    T[3] = float(input("Introduzca la nota del examen teórico 4: "))
    # ---------
    P[0] = float(input("Introduzca la nota del examen práctico 1: "))
    P[1] = float(input("Introduzca la nota del examen práctico 2: "))

    NC1 = nota_cuatrimestre(T[0], T[1], P[0])
    NT1 = nota_teoria(T[0], T[1])

    NC2 = nota_cuatrimestre(T[2], T[3], P[1])
    NT2 = nota_teoria(T[2], T[3])

    NF = nota_continua(NC1, NC2)

    return (
        f"Hola {nombre} , Estamos calculando tus notas... \n"
        f"las notas del primer cuatri son teoria {NT1} , practica {P[0]} , NOTA CUAT1 {NC1}\n"
        f"Tus notas del segundo cuatrimestre son: teoria {NT2} , practica {P[1]} , NOTA CUAT2 {NC2}\n"
        f"Tu nota final de la asignatura es {NF}"
    )

def main() -> None:
    print("empzando el programa ....")
    print(solicita_notas())


if __name__ == "__main__":
    main()
