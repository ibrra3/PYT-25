"""
repositorio, propietario, lenguajes, privado, commits
ProjectX,user123,"Python,JavaScript",True,[b789101#Initial commit#2023-10-06
12:00:00;c567891#Added main functionality#2023-10-06 13:00:00]
MiFirstRepo,newbie,"Go",False,[]
"""
#from collections import Counter
from csv import reader
from typing import NamedTuple, List, Set, Tuple, Dict, Optional
from datetime import datetime, date

Commit = NamedTuple(
    "Commit",
    [
        ("id", str),  # Identificador alfanumérico del commit
        ("mensaje", str),  # Mensaje asociado al commit
        ("fecha_hora", datetime),  # Fecha y hora en la que se registró el commit
    ],
)
Repositorio = NamedTuple(
    "Repositorio",
    [
        ("nombre", str),  # Nombre del repositorio
        ("propietario", str),  # Nombre del usuario propietario
        ("lenguajes", Set[str]),  # Conjunto de lenguajes usados
        ("privado", bool),  # Indica si es privado o público
        ("commits", List[Commit]),  # Lista de commits realizados
    ],
)


def parsea_commits(commits_str: str) -> List[Commit]:
    # [g345671#Setup project#2023-10-06 12:00:00;h456781#Added frontend#2023-10-06 12:01:00]
    # ------------------------------------------------------------------------------------------------------------       parsea_commits
    """
    el formato esperado de la cadena recibida como parámetro separa la información de cada
    commit por punto y coma (;). Además, para cada commit, el identificador, el mensaje y la fecha/hora
    están separados por #. Si la cadena recibida es “[]”, la función devuelve una lista vacía.
    """
    res = []
    if commits_str == "[]":
        return []

    commits_str = commits_str.strip("[]")
    commits = commits_str.split(";")

    for commit in commits:
        commits_split = commit.split("#")
        id = str(commits_split[0])
        mensaje = str(commits_split[1])
        fecha_hora = datetime.strptime(commits_split[2], "%Y-%m-%d %H:%M:%S")
        res.append(Commit(id, mensaje, fecha_hora))
    return res


# ------------------------------------------------------------------------------------------------------------       lee_repositorios
def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    """
    lee_repositorios: dada una cadena de texto con la ruta de un fichero CSV, devuelve una lista de tuplas de
    tipo Repositorio con la información contenida en el fichero."""

    """
    repositorio, propietario, lenguajes, privado, commits
    ProjectX,user123,"Python,JavaScript",True,[b789101#Initial commit#2023-10-06
    12:00:00;c567891#Added main functionality#2023-10-06 13:00:00]
    MiFirstRepo,newbie,"Go",False,[]
    """
    res = []
    with open(csv_filename, encoding="utf-8") as fichero:
        lector = reader(fichero, delimiter=",")
        next(lector)
        for repositorio, propietario, lenguajes, privado, commits in lector:

            nombre = str(repositorio)
            propietario = str(propietario)
            lenguajes = set(lenguajes.strip().split(","))
            privado = privado.strip().lower() == "true"
            commits = parsea_commits(commits)
            res.append(Repositorio(nombre, propietario, lenguajes, privado, commits))
        return res


Commit = NamedTuple(
    "Commit",
    [
        ("id", str),  # Identificador alfanumérico del commit
        ("mensaje", str),  # Mensaje asociado al commit
        ("fecha_hora", datetime),  # Fecha y hora en la que se registró el commit
    ],
)
Repositorio = NamedTuple(
    "Repositorio",
    [
        ("nombre", str),  # Nombre del repositorio
        ("propietario", str),  # Nombre del usuario propietario
        ("lenguajes", Set[str]),  # Conjunto de lenguajes usados
        ("privado", bool),  # Indica si es privado o público
        ("commits", List[Commit]),  # Lista de commits realizados
    ],
)


# ------------------------------------------------------------------------------------------------------------       total_commits_por_anyo


def total_commits_por_anyo(repositorios: List[Repositorio]) -> Dict[int, int]:
    """
    total_commits_por_anyo: dada una lista de tuplas de tipo Repositorio, devuelve un diccionario en el que
    las claves son los años, y los valores el número total de commits registrados en el año dado como clave para
    los repositorios públicos.
    """
    # dict{anyo:commits publicos}
    repositorios_publicos = [
        repositorio for repositorio in repositorios if not repositorio.privado
    ]
    anyos = {}
    for repositorio in repositorios_publicos:
        for commit in repositorio.commits:
            anyo = commit.fecha_hora.year
            if anyo not in anyos:
                anyos[anyo] = 0
            anyos[anyo] += 1
    return anyos


# ------------------------------------------------------------------------------------------------------------          calcular_tasa_crecimiento

def calcular_tasa_crecimiento(repositorio: Repositorio) -> float:
    '''
    calcular_tasa_crecimiento: dado un Repositorio, devuelve su tasa de crecimiento. La tasa de
    crecimiento de un repositorio se define como la ratio entre el número de commits y el número de
    días transcurridos entre el primer y el último commit (los commits están ordenados en el archivo). Si
    el repositorio tiene menos de 2 commits, o si tiene 2 o más commits pero no ha pasado al menos un
    día entre el primero y el último, la tasa se considera cero'''

    #Ayuda: Los días transcurridos entre dos variables dt1 y dt2, de tipo datetime, se pueden calcular como (dt2-dt1).days.

    #tasa de crecimiento = numero_commits / dias entre el primer y ultimo commit     

    if len(repositorio.commits)<2:
        return 0.0
    
    numero_commits = len(repositorio.commits)
    fecha_in = repositorio.commits[0].fecha_hora
    fecha_fin = repositorio.commits[-1].fecha_hora
    dias = (fecha_fin-fecha_in).days
    
    if dias <1:
        return 0.0
    
    
    tasa = numero_commits/dias 
    return tasa 

# ------------------------------------------------------------------------------------------------------------ n_mejores_repos_por_tasa_crecimiento

def n_mejores_repos_por_tasa_crecimiento( repositorios: List[Repositorio], n: Optional[int] = 3) -> List[Tuple[str, float]]:
    """
    n_mejores_repos_por_tasa_crecimiento: dada una lista de tuplas de tipo Repositorio y un número
    entero n (con valor por defecto igual a 3), devuelve una lista con los n nombres de los repositorios y sus tasas
    de crecimiento más altas"""

    #sorted , lambda , reverse 
    tasas=[]
    repositorios_tasas=[repositorio for repositorio in repositorios]

    for repositorio in repositorios_tasas:
        nombre = repositorio.nombre
        tasa = calcular_tasa_crecimiento(repositorio)
        tasas.append((nombre,tasa))

    tasas_ordenadas = sorted (tasas , key = lambda x:x[1] , reverse=True )
    
    return tasas_ordenadas[:n]


# ------------------------------------------------------------------------------------------------------------ 

def recomendar_lenguajes (repositorios:List[Repositorio],repositorio:Repositorio)->Set[str]:



    '''recomendar_lenguajes: dada una lista de tuplas de tipo Repositorio y un repositorio específico, devuelve
    un conjunto con los lenguajes de programación recomendados para dicho repositorio. Los lenguajes
    recomendados son aquellos que se usan en repositorios similares al repositorio dado. Se considera que un
    repositorio es similar al dado si comparte al menos uno de los lenguajes de programación con el repositorio
    dado. Por ejemplo, si queremos hacer una recomendación para el repositorio "LAB-FP", cuyo lenguaje es Java,
    podemos considerar similar el repositorio "LAB-Calificaciones", que utiliza Java y Python, ya que ambos
    -4-
    comparten el lenguaje Java. En este caso, se recomendaría Python como nuevo lenguaje para el repositorio
    "LAB-FP".
'''
















