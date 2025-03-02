# this is an attack by SK2

from collections import namedtuple
from csv import reader


Audiencia = namedtuple("Audiencia", "edicion, share")

"""
    La edición a la que pertenece el programa
    El share (porcentaje de la audiencia que vio ese programa concreto)
    [edicion,porcentaje]
    1,0.37
    1,0.33
    1,0.47
    1,0.46
    1,0.54
    1,0.43
    1,0.59
    1,0.58
"""


def lee_Audiencia(ruta: str) -> list[Audiencia]:
    """
    Lee el fichero de entrada y devuelve una lista de audiencias
    """

    with open(ruta, encoding="utf-8") as fichero:
        lector = reader(fichero, delimiter=",")
        # next(lector)
        res = []
        for edicion, share in lector:
            edicion = int(edicion)
            share = float(share)
            share = round(share * 100, 1)
            # share = f"{(share*100):.1f}%"
            cadena = Audiencia(edicion, share)
            res.append(cadena)
        return res


def nada():
    """
    En este bloque queremos responder a tres preguntas distintas:

    ¿Cuántas ediciones tiene el programa del que queremos analizar la audiencia?
    ¿Qué audiencias han tenido todas las emisiones del programa de una edición concreta?
    ¿Cuál es la media de share en cada una de las ediciones?"""
    return None


def calcular_ediciones(audiencias: list[Audiencia]) -> int:
    """
    cuentas las ediciones totales"""
    res = 0
    set_edicion = set()
    # para el programa GRAN HERMANO
    for audiencia in audiencias:
        set_edicion.add(audiencia.edicion)
    res += len(set_edicion)
    return res


def filtra_audiencias(
    audiencias: list[Audiencia], ediciones: set[int]
) -> list[Audiencia]:
    """
    filtra las audiencias por un set de ediciones dado"""
    res = []
    for audiencia in audiencias:
        if audiencia.edicion in ediciones:
            res.append(audiencia)
    return res


def media_porcentaje_por_audiencia(
    audiencias: list[Audiencia], edicion: int
) -> list[float]:

    porcentajes = []
    for audiencia in audiencias:
        if audiencia.edicion == edicion:
            porcentajes.append(audiencia.share)
    return sum(porcentajes) / len(porcentajes)


def porcentaje_edicion(audiencias: list[Audiencia]):
    """
    devuelve cada edicion con la media de porcentajes que tiene"""
    ediciones = {}
    for audiencia in audiencias:
        if audiencia.edicion not in ediciones:
            ediciones[audiencia.edicion] = 0
        ediciones[audiencia.edicion] = media_porcentaje_por_audiencia(
            audiencias, audiencia.edicion
        )
    return ediciones
