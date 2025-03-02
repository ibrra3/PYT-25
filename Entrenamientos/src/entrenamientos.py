import csv
from datetime import *
from collections import namedtuple

Entrenamientos = namedtuple(
    "Entreno",
    "tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido",
)


def lee_entrenamientos(ruta: str) -> list[Entrenamientos]:
    result = []
    with open(ruta, encoding="UTF-8") as f:

        lector = csv.reader(f)
        next(lector)

        for linea in lector:
            tipo = linea[0]
            fechahora = datetime.strptime(linea[1], "%d/%m/%Y %H:%M")
            ubicacion = linea[2]
            duracion = int(linea[3])
            calorias = int(linea[4])
            distancia = float(linea[5])
            frecuencia = int(linea[6])
            compartido = linea[7]
            cadena = Entrenamientos(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido,)
            result.append(cadena)

    return result


def test_entrenos(ruta: str, lineas: int):

    entrenos = lee_entrenamientos(ruta)

    print(f"los primeros {lineas} registros son: \n")
    for entreno in entrenos[:lineas]:
        print(entreno)

    print(f"los ultimos {lineas} registros son: \n")
    for entreno in entrenos[-lineas:]:
        print(entreno)



def test_entrenos2(ruta: str, lineas: int):

    entrenos = lee_entrenamientos(ruta)
    primeras = entrenos[:lineas]
    ultimas = entrenos[-lineas:]
    # --------------------------------------  QUIERO SALTO DE LINEA , NO VA !!
    print(f"los primeros {lineas} registros son: \n{primeras}")
    print(f"\nlos ultimos {lineas} registros son:\n {ultimas}")


   
