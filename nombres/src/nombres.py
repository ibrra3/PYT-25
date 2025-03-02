# PROYECTO NOMBRES
"""
Año,Nombre,Frecuencia,Género
2002,DAVE FREE,8020,Hombre
2002,PABLO,5799,Hombre
2002,DANIEL,5603,Hombre
2002,DAVID,5414,Hombre
"""

# FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')
# leer_frecuencias_nombres:
"""recibe la ruta de un fichero CSV codificado en UTF-8, 
y devuelve una lista de tuplas de tipo FrecuenciaNombre(int, str, int, str) 
conteniendo todos los datos almacenados en el fichero."""


import csv
from collections import namedtuple

# ---------------------------------------------------------------------------------------------------------------------------------
FrecuenciaNombre = namedtuple("FrecuenciaNombre", "ano , nombre , frecuencia , genero ")
# ------------------------------------------------------------------------------------------------------------------------------------------------------


def lee_frecuencias_nombres(ruta: str) -> list[FrecuenciaNombre]:

    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        res = []
        for linea in lector:
            ano = int(linea[0])
            nombre = str(linea[1])
            frecuencia = int(linea[2])
            genero = str(linea[3])
            cadena = FrecuenciaNombre(ano, nombre, frecuencia, genero)
            res.append(cadena)
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def filtrar_por_genero(
    frecuencias: list[FrecuenciaNombre], genero: str = None
) -> list[
    FrecuenciaNombre
]:  # filtra una frecuencia segun el genero[ HOMBRE , MUJER , NONE]
    res = []
    for registro in frecuencias:
        if registro.genero == genero or genero is None:
            res.append(registro)
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_nombres(
    frecuencias: list[FrecuenciaNombre], genero: str = None
) -> set[str]:  # devuelve lista filtrada de nombres segun genero que puede ser none
    res = set()

    for registro in frecuencias:
        if genero is None or registro.genero == genero:
            res.add(registro)

    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def filtra_nombres_genero_ano(
    frecuencias: list[FrecuenciaNombre], ano: int, genero: str = None
) -> list[FrecuenciaNombre]:
    '''filtra segun un nombre y genero dado, devuelve lista frecuencias '''
    res = []
    
    res1 = filtrar_por_genero(frecuencias, genero)

    for registro in res1:
        if registro.ano == ano:
            res.append(registro)

    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def sacar_nombres(frecuencias: list[FrecuenciaNombre]) -> list[str]:
    res = []
    for (
        regisro
    ) in (
        frecuencias
    ):  #                         SACA LOS NOMBRES DE UNA LISTA FRECUENCIAS NOMBRE ! ! !
        res.append(regisro.nombre)
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def top_nombre_ano(
    frecuencias: list[FrecuenciaNombre], ano: int, limite: int = 10, genero: str = None
) -> list[tuple[str, int]]:
    """
    recibe una lista de tuplas de tipo FrecuenciaNombre, un año de tipo int, un número límite de tipo int y un género de tipo str,
    y devuelve una lista de tuplas (nombre, frecuencia) de tipo (str, int) con los nombres más frecuentes del año y el género dados,
    ordenada de mayor a menor frecuencia, y con un máximo de límite nombres. El género puede ser 'Hombre', 'Mujer' o tener un valor None,
    en cuyo caso se incluyen en la lista todos los nombres. El valor por defecto del límite es 10 y el del género es None.
    """
    res2 = set()
    res1 = filtra_nombres_genero_ano(frecuencias, ano, genero)
    for registro in res1:
        res2.add((registro.nombre, registro.frecuencia))
    return sorted(res2, key=lambda x: x[1], reverse=True)


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_nombres_ambos_generos(frecuencias: list[FrecuenciaNombre]) -> set[str]:
    """recibe una lista de tuplas de tipo FrecuenciaNombre, y
    devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
    """
    hombres = filtrar_por_genero(frecuencias, "Hombre")
    mujeres = filtrar_por_genero(frecuencias, "Mujer")

    nombresH = sacar_nombres(hombres)
    nombresM = sacar_nombres(mujeres)

    res = set()

    for nombres in nombresH:
        if nombres in nombresM:
            res.add(nombres)
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def fuck_you():
    print("FUCK THIS SHIT IM OUT ")
    # USE ONLY WHEN YOU´RE TIERD


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_nombres_compuestos(
    frecuencias: list[FrecuenciaNombre], genero: str = None
) -> set[str]:
    """calcular_nombres_compuestos: recibe una lista de tuplas de tipo FrecuenciaNombre y
    un género de tipo str, y devuelve un conjunto {str} con los nombres que contienen más de una palabra.
    El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en el conjunto todos los nombres.
    El valor por defecto del género es None."""

    res1 = filtrar_por_genero(frecuencias, genero)
    res2 = sacar_nombres(res1)
    res3 = set()
    for nombre in res2:
        if " " in nombre:
            res3.add(nombre)
    return res3


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_nombres_compuestos2(
    frecuencias: list[FrecuenciaNombre], genero: str = None
) -> set[str]:
    """calcular_nombres_compuestos: recibe una lista de tuplas de tipo FrecuenciaNombre y
    un género de tipo str, y devuelve un conjunto {str} con los nombres que contienen más de una palabra.
    El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso se incluyen en el conjunto todos los nombres.
    El valor por defecto del género es None."""

    res1 = filtrar_por_genero(frecuencias, genero)
    res2 = sacar_nombres(res1)
    res3 = set()
    for nombre in res2:
        if (
            len(nombre.split()) > 1
        ):  # split hace que si dos palabras estan separadas por un espacio que se consideren de longitud 2
            res3.add(nombre)
    return res3


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def filtra_anos(
    frecuencias: list[FrecuenciaNombre], ano_i: int, ano_f: int
) -> list[FrecuenciaNombre]:

    res = []
    if (ano_i > 2001) and (ano_i < ano_f) and (ano_f < 2018):
        for registro in frecuencias:
            if ano_i <= registro.ano <= ano_f:
                res.append(registro)
    else:
        res = None

    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------
def frecuencia(frecuencias: list[FrecuenciaNombre]) -> list[int]:
    res = []  # ---------------------------------           NO ES NECESARIO
    for registro in frecuencias:
        res.append(registro.frecuencia)
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_frecuencia_media_nombre_años(
    frecuencias: list[FrecuenciaNombre], nombre: str, ano_i: int, ano_f: int
) -> float:
    """
    calcular_frecuencia_media_nombre_años: recibe una lista de tuplas de tipo FrecuenciaNombre,
    un nombre, un año inicial y un año final y calcula la frecuencia media del nombre dado como
    parámetro en el rango de años [año_inicial, año_final) formado por el año inicial y el año final dados como parámetro.
    Si no se puede calcular la media devuelve 0.
    """

    res1 = filtra_anos(
        frecuencias, ano_i, ano_f
    )  # lista FrecuenciaNombre filtrada por el rango de anos dado
    if res1 is None or len(res1) == 0:
        return f"ha habido un problema en el filtrado de anos , comprueba el intervalo{None}"

    res2 = []  # LISTA de las frecuencias del nombre por ano

    for registro in res1:
        if registro.nombre == nombre:
            res2.append(registro.frecuencia)
            res = sum(res2) / len(res2)
    if len(res2) == 0:
        return f"ha habido un problema en la media de frecuencias , puede que el nombre no este en el intervalo de anos comprueba el intervalo{None}"
    return res


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_nombre_mas_frecuente_año_genero(
    frecuencias: list[FrecuenciaNombre], ano: int, genero: str
) -> str:
    """recibe una lista de tuplas de tipo FrecuenciaNombre,
    un año y un género y devuelve el nombre más frecuente en el año dado como parámetro del género dado como parámetro.
    """
    res1 = []
    dato1 = filtra_nombres_genero_ano(frecuencias, ano, genero)

    for registro in dato1:
        res1.append((registro.nombre, registro.frecuencia))

    return max(res1, key=lambda n: n[1])


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_año_mas_frecuencia_nombre(
    frecuencias: list[FrecuenciaNombre], nombre: str
) -> list[FrecuenciaNombre]:
    """
    recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre y devuelve el año con mayor frecuencia del nombre dado como parámetro
    """
    res = []
    for registro in frecuencias:
        if registro.nombre == nombre:
            res.append((registro.nombre, registro.ano, registro.frecuencia))
    dato = max(res, key=lambda n: n[2])
    return dato[1]


# ------------------------------------------------------------------------------------------------------------------------------------------------------
def calcular_nombres_mas_frecuentes(
    frecuencias: list[FrecuenciaNombre], genero: str, decada: int, n: int = 5
) -> list[str]:
    """
    : recibe una lsta de tuplas de tipo FrecuenciaNombre,
    un género, un entero que reresenta una década y un número n y devuelve una lista con los n nombres más frecuentes,
    de mayor a menor frecuencia, del un género dado en la década dada. Por defecto, debe devolver los 5 más frecuentes.
    La década se da con cuatro dígitos: 1960, 1970...
    """
    dato1 = filtrar_por_genero(frecuencias, genero)
    dato2 = []
    for registro in dato1:
        if registro.ano in [decada, decada + 10]:
            dato2.append((registro.nombre, registro.frecuencia))

    res = sorted(dato2, key=lambda x: x[1], reverse=True)

    return res[:n]

# ---------------------------------------------------------------------------------------------------------------------------
# filter function

'''
lista_notas = [54, 43, 76, 56, 98, 32, 43]
x = map(lambda n :n+1 , lista_notas)
print(list(x))
'''
#........................................................
"""
lista_notas = [54, 43, 76, 56, 98, 32, 43]


def filtra_nota(nota: list[int]) -> bool:
    return nota >= 60


def mapear_notas (nota):
    if nota>=60:
        return nota 
#....................................................
notas_map = list(map(mapear_notas,lista_notas))
print(notas_map)    
#........................................................
notas_filtrada = list(filter(filtra_nota, lista_notas))
print(notas_filtrada)
#........................................................
nota_filter_lambda = list(filter(lambda n: n >= 60, lista_notas))   #      -------  ESTA ES MEJOR 
print(nota_filter_lambda)
"""
# -------------------------------------------------------------------------------------------------------------------------
'''
#print(help(filtra_nombres_genero_ano))
#%%
print(help(range))
# %%
'''

#%% print ("hi")