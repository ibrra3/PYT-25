# FUCK COPILOT
# THIS IS AN ATTACK BY SK-2
# SK[D.A]
"""
duracion en segundos
datetime,city,state,shape,duration,comments,latitude,longitude
07/04/2011 22:00,muncie,in,light,240, ((HOAX??)) 4th  of July ufo...,40.1933333,-85.3863889
04/07/2005 17:01,deming (somewhere near),nm,changing,1200, ((NUFORC...,32.2686111,-107.7580556
03/12/2010 19:56,erie,pa,changing,300, 3/12/10Viewed a comet like...,42.1291667,-80.0852778
07/04/2013 22:25,seattle,wa,unknown,600, A RED Light was seen over...,47.6063889,-122.3308333
"""
from collections import namedtuple
from csv import reader
from datetime import datetime
from datetime import date
from math import sqrt
from collections import Counter
ovnis = namedtuple(
    "ovnis", "fecha, ciudad, estado, forma, duracion, comentarios, coordenadas"
)

Coordenadas = namedtuple("coordenadas", "latitud,longitud")

from calendar import month_name


def lee_ovnis(ruta) -> list[ovnis]:
    with open(ruta, encoding="utf-8") as file:
        lector = reader(file)
        next(lector)
        res = []
        for (
            fecha,
            ciudad,
            estado,
            forma,
            duracion,
            comentarios,
            latitud,
            longitud,
        ) in lector:
            fecha = str(fecha)
            fecha = datetime.strptime(fecha, "%m/%d/%Y %H:%M")
            ciudad = str(ciudad.strip())
            estado = str(estado.strip())
            forma = str(forma.strip())
            duracion = int(duracion.strip())
            comentarios = str(comentarios.strip())
            latitud = float(latitud.strip())
            longitud = float(longitud.strip())
            coordenadas = Coordenadas(latitud, longitud)
            cadena = ovnis(
                fecha, ciudad, estado, forma, duracion, comentarios, coordenadas
            )
            res.append(cadena)
        return res


def numero_avistamientos_fecha(ovnis: list[ovnis], fecha: datetime.date) -> int:
    """
    numero_avistamientos_fecha: Función que obtiene el número total de avistamientos que se han producido en una fecha determinada,
    dada por su día, mes y año. Se contarán, por tanto, los avistamientos que hayan tenido lugar a cualquier hora del día.
    La función recibe una lista de namedtuple de tipo Avistamiento, y una fecha de tipo datetime.date.
    """
    res = []
    for registro in ovnis:
        if registro.fecha.date() == fecha:
            res.append(registro)
    return len(res)


def formas_estados(ovnis: list[ovnis], estados: set[str]) -> int:
    """
    ormas_estados: Función que obtiene el número de formas distintas que presentaron
    los avistamientos observados en uno o varios estados.
    La función recibe una lista de namedtuple de tipo Avistamiento, y un conjunto de estados de tipo str.
    """

    res = set()
    for registro in ovnis:
        if registro.estado in estados:
            res.add(registro.forma)
    return len(res)


def duracion_total(ovnis: list[ovnis], estado: str) -> int:
    """
    duracion_total: Función que devuelve la duración total en segundos de los avistamientos que se
    han observado en un estado. La función recibe una lista de namedtuple de tipo Avistamiento, y
    un estado de tipo str."""

    """res=0
    for registro in ovnis :
        if registro.estado == estado:
            res+=registro.duracion
    return res """

    filtro = [registro.duracion for registro in ovnis if registro.estado == estado]
    return sum(filtro)


def distancia_coords(c1: Coordenadas, c2: Coordenadas) -> float:
    """
    distancia: Función que calcula la distancia euclidea entre dos coordenadas.
    La función recibe dos tuplas de tipo (float, float)."""
    # Coordenadas(latitud,longitud)
    latitud = c1.latitud - c2.latitud
    longitud = c1.longitud - c2.longitud
    distance = sqrt(latitud**2 + longitud**2)

    return distance


def avistamientos_cercanos_ubicacion(
    ovnis: list[ovnis], ubicacion: Coordenadas, radio: float
) -> list[ovnis]:
    """
    avistamientos_cercanos_ubicacion: Función que calcula un conjunto con los avistamientos cercanos a una ubicacion dada.
    Concretamente, vamos a obtener los avistamientos que se encuentren dentro de un determinado radio de distancia de la ubicación.
    La función recibe una lista de namedtuple de tipo Avistamiento, una ubicación que será una tupla de tipo (float, float),
    y una distancia de tipo float"""
    # filtro = filter(distancia(registro.coordenadas , ubicacion) , registro in ovnis)

    filtro = filter(
        lambda ovni: distancia_coords(ovni.coordenadas, ubicacion) < radio, ovnis
    )
    res = list(filtro)
    return res  # , len(res)


def avistamiento_mayor_duracion(ovnis: list[ovnis], forma: str) -> list[ovnis]:
    """
    avistamiento_mayor_duracion: Función que obtiene el avistamiento de mayor duración de entre todos los avistamientos que tienen una forma determinada.
    La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo str.
    """

    ovnis_forma = [ovni for ovni in ovnis if ovni.forma == forma]
    # ovnis_duracion = map(lambda ovni:ovni.duracion, ovnis_forma)
    ovni_maximo = max(ovnis_forma, key=lambda ovni: ovni.duracion)
    return ovni_maximo


def avistamiento_cercano_mayor_duracion(
    ovnis: list[ovnis], ubi: Coordenadas, radio: float
):
    """
    avistamiento_cercano_mayor_duracion: Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de
    un radio de distancia de una ubicación dada; es decir, la distancia entre las coordenadas del avistamiento y
    las coordenadas que se pasan como parámetro de entrada debe ser menor al radio que también aparece como parámetro de la función.
    El resultado debe ser una tupla de la forma (duración, comentarios). La función recibe una lista de namedtuple de tipo Avistamiento,
    una coordenada que será una tupla de tipo (float, float), y una distancia de tipo float.
    """

    avistamientos_cercanos = avistamientos_cercanos_ubicacion(ovnis, ubi, radio)
    ovni_max = max(avistamientos_cercanos, key=lambda ovni: ovni.duracion)
    # (duración, comentarios)
    # ovni_duracion_coment = map(lambda ovni : (ovni.duracion, ovni.comentario) , ovni_max)
    ovni_duracion_coment = [ovni_max.duracion, ovni_max.comentarios]
    return list(ovni_duracion_coment)


def avistamientos_fechas(
    ovnis: list[ovnis], fechain: datetime, fechafin: datetime
) -> list[ovnis]:
    """
    avistamientos_fechas: Función que devuelve una lista con los avistamientos observados entre una fecha inicial y
    una fecha final, ambas inclusive. La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos.
    Si la fecha inicial es None, se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es None,
    se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son None,
    se devolverá la lista de avistamientos completa. La función recibe una lista de namedtuple de tipo Avistamiento,
    y dos fechas de tipo datetime.date: una como principio del intervalo y otra como final. Las fechas recibidas
    como parámetro tendrán como valor por defecto None."""

    res = []
    if fechafin is None and fechain is None:
        res = [ovni for ovni in ovnis]
        return sorted(res, key=lambda res: res.fecha, reverse=True)

    if fechafin is None:
        # . Si la fecha final es None, se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente.
        """for ovni in ovnis:
        if fechain<=ovni.fecha.date():
            res.append(ovni)"""
        res = [ovni for ovni in ovnis if fechain <= ovni.fecha.date()]
        return sorted(res, key=lambda res: res.fecha, reverse=True)

    elif fechain is None:
        """fechain=date(0,0,0)
        for ovni in ovnis:
            if ovni.fecha.date()<=fechafin:
                res.append(ovni)"""
        res = [ovni for ovni in ovnis if ovni.fecha.date() <= fechafin]
        return sorted(res, key=lambda res: res.fecha, reverse=True)

    """for ovni in ovnis: 
        if fechain<=ovni.fecha.date()<=fechafin:
            res.append(ovni)"""
    res = [ovni for ovni in ovnis if fechain <= ovni.fecha.date() <= fechafin]
    """
    res = [
        ovni for ovni in ovnis
        if (fechain is None or ovni.fecha.date() >= fechain) and #------GPT !!--------
           (fechafin is None or ovni.fecha.date() <= fechafin)
    ]"""
    return sorted(res, key=lambda res: res.fecha, reverse=True)


def saca_comentario(ovnis: ovnis) -> list[str]:
    """THIS FUCNTION IS USSLESS"""
    res = [(ovni.comentarios).split() for ovni in ovnis]
    return res


def comentario_mas_largo(ovnis: list[ovnis], anyo: int, palabra: str) -> list[ovnis]:
    """
    comentario_mas_largo: Función que devuelve el avistamiento con el comentario más largo, de entre todos los
    avistamientos observados en un año dado y cuyo comentario incluye una palabra concreta.
    La función recibe una lista de namedtuple de tipo Avistamiento, un año de tipo int, y una palabra de tipo str.
    """

    res = [
        ovni
        for ovni in ovnis
        if (ovni.fecha.year == anyo) and palabra.lower() in ovni.comentarios.lower()
    ]
    return max(
        res, key=lambda res: len(res.comentarios)
    )  # ,min(res, key= lambda res :len(res.comentarios))


def media_dias_entre_avistamientos(ovnis: list[ovnis], anyo: int = None) -> float:
    """
    media_dias_entre_avistamientos: Función que devuelve la media de días transcurridos
    entre dos avistamientos consecutivos en el tiempo. La función permite hacer el cálculo para todos los avistamientos,
    o solo para los de un año concreto. La función recibe una lista de namedtuple de tipo Avistamiento y un año de tipo int.
    """
    if not ovnis or len(ovnis) < 2:
        return 0.0
    lista_ovnis = [ovni for ovni in ovnis if anyo is None or ovni.fecha.year == anyo]
    sorted_ovnis = sorted(
        lista_ovnis, key=lambda lista_ovnis: lista_ovnis.fecha, reverse=False
    )
    # OR lista_ovnis.sort(key=lambda ovni: ovni.fecha)

    # INCORRECTO !! diferencia = [(ovni[i].fecha - ovni[i-1].fecha).days for ovni in lista_ovnis for i in range(i,len(lista_ovnis))]
    diferencia = [
        (sorted_ovnis[i].fecha - sorted_ovnis[i - 1].fecha).days
        for i in range(1, len(sorted_ovnis))
    ]

    return sum(diferencia) / len(diferencia)


def cuenta_ovnis_anyo(ovnis: list[ovnis], year: int) -> int:
    res = [ovni for ovni in ovnis if year is None or ovni.fecha.year == year]
    return len(res)


def avistamientos_por_fecha(ovnis: list[ovnis]) -> dict[datetime, ovnis]:
    """
    avistamientos_por_fecha: Función que crea un diccionario que relaciona las fechas con
    los avistamientos observados en dichas fechas. Es decir, un diccionario cuyas claves son las fechas y
    cuyos valores son los conjuntos de avistamientos observados en cada fecha.
    La función recibe una lista de namedtuple de tipo Avistamiento."""
    """
    clave_fechas={}
    for ovni in ovnis :
        fecha=ovni.fecha.date()
        if fecha not in clave_fechas:
            clave_fechas[fecha]=set()
        clave_fechas.add(ovni)
        return clave_fechas"""
    fechas = {}
    for ovni in ovnis:
        if ovni.fecha.date() not in fechas:
            fechas[ovni.fecha.date()] = set()
        fechas[ovni.fecha.date()].add(ovni)
    return fechas


def formas_por_mes(ovnis: list[ovnis]) -> dict[datetime, set[str]]:
    """
    formas_por_mes: Función que devuelve un diccionario que indexa las distintas formas de avistamientos
    por los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un
    conjunto con todas las formas distintas observadas en dicho mes.
    La función recibe una lista de namedtuple de tipo Avistamiento."""

    meses = {}
    for ovni in ovnis: 
        mes = ovni.fecha.month
        if mes not in meses:
            meses[mes] = set()
        meses[mes].add(ovni.forma)
    meses_ordenados = {key: meses[mes] for key in sorted(meses.keys())}
    meses_nombres = {
        month_name[key]: meses_ordenados[key] for key in meses_ordenados.keys()
    }
    return meses_nombres


# meses_ordenados[key] returns the value in the key not the key !!!!!!

def formas_por_mes2 (ovnis:list[ovnis])->dict[str:set[str]]:
    
    meses={month_name[i]: set() for i in range(1,13)}
    for ovni in ovnis:
        mes = ovni.fecha.month
        meses[month_name[mes]].add(ovni.forma)
    return meses     

def fromas_mes(ovnis: list[ovnis]) -> dict[str, set[str]]:

    meses = {}
    for ovni in ovnis:
        mes = ovni.fecha.month
        if mes not in meses:
            meses[mes] = set()
        meses[mes].add(ovni.forma)
    meses_ordenados = {month_name[key]: meses[key] for key in sorted(meses.keys())}
    return meses_ordenados


def numero_avistamientos_por_año(ovnis: list[ovnis]) -> dict[int, int]:
    """

    numero_avistamientos_por_año: Función que crea un diccionario que relaciona cada año con el número
    de avistamientos observados en dicho año. Es decir, un diccionario cuyas claves son los años y
    cuyos valores son el número de avistamientos observados en cada año.
    La función recibe una lista de namedtuple de tipo Avistamiento."""
    anyos ={}
    for ovni in ovnis : 
        anyo = ovni.fecha.year
        if anyo not in anyos:
            anyos[anyo]=0
        anyos[anyo]+=1 #if anyo in anyos !
        anyos_ordenados = {key:anyos[key] for key in sorted(anyos.keys())}
    return anyos_ordenados    


def num_avistamientos_por_mes(ovnis:list[ovnis])->dict[int,int]:
    '''
    num_avistamientos_por_mes: Función que devuelve el número de avistamientos observados en cada mes del año. 
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:
            "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", 
            "Octubre", "Noviembre", "Diciembre"]'''
    meses={}
    for ovni in ovnis:
        mes=ovni.fecha.month
        if mes not  in meses:
            meses[mes]=0
        meses[mes]+=1 #if mes in meses!
    meses_ordenados = {key:meses[key] for key in sorted(meses.keys())}
    return meses_ordenados

def num_avistamientos_por_mes2 (ovnis:list[ovnis])->dict[str,int]:
    
    meses ={month_name[i]:0 for i in range(1,13)}
    
    for ovni in ovnis:
        ovni.coordenadas
        mes=ovni.fecha.month
        #meses[month_name[mes]]=0  !! WRONG!!! 
        meses[month_name[mes]]+=1
    return meses

def coordenadas_mas_avistamientos(ovnis:list[ovnis])->tuple[int,int]:
    '''
    coordenadas_mas_avistamientos: Función que devuelve las coordenadas enteras que se 
    corresponden con la zona donde más avistamientos se han observado. Por ejemplo, si hay avistamientos 
    en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), la zona con más avistamientos
    corresponde a las coordenadas enteras (40, -85) con 2 avistamientos.'''
    
    int_cords = [(int(ovni.coordenadas.latitud),int(ovni.coordenadas.longitud)) for ovni in ovnis]
    coords=Counter(int_cords)
    #return coords.most_common(1)[0][0] if coords.most_common else None
    return coords.most_common(1)[0][0]

def hora_mas_avistamientos(ovnis:list[ovnis])->int:
    '''
    hora_mas_avistamientos: Función que devuelve la hora del día (de 0 a 23) en la que se han observado 
    un mayor número de avistamientos.'''
    horas=[]
    for ovni in ovnis:
        hora=ovni.fecha.hour
        horas.append(hora)
    contador_horas = Counter(horas)
    return contador_horas.most_common(1)[0][0]
###########
from collections import Counter


def longitud_media_comentarios_por_estado(ovnis:list[ovnis])->dict[str:float]:
    '''
    longitud_media_comentarios_por_estado: Función que devuelve un diccionario en el que las claves son los estados 
    donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos
    observados en cada estado.'''
    
    estados={}
    for ovni in ovnis:
        estado = ovni.estado
        if estado not in estados:
            estados[estado]=0.0
        estados[estado]=(sum([ovni.comentarios.split() for ovni in ovnis])/len([ovni.comentarios.split() for ovni in ovnis]))    
    return estados
##########################################################################################################################################
def longitud_media_comentarios_por_estado(ovnis: list[ovnis]) -> dict[str, float]:
    '''
    longitud_media_comentarios_por_estado: Función que devuelve un diccionario en el que las claves son los estados 
    donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos
    observados en cada estado.
    '''
    estados = {}

    # Inicializar un diccionario para almacenar la suma de longitudes y el número de comentarios por estado
    sumas_y_contadores = {}
    for ovni in ovnis:
        estado = ovni.estado
        longitud_comentario = len(ovni.comentarios)
        if estado not in sumas_y_contadores:
            sumas_y_contadores[estado] = [0, 0]  # [suma_longitudes, cantidad_comentarios]
        sumas_y_contadores[estado][0] += longitud_comentario
        sumas_y_contadores[estado][1] += 1

    # Calcular la media de longitudes para cada estado
    for estado, (suma_longitudes, cantidad) in sumas_y_contadores.items():
        estados[estado] = suma_longitudes / cantidad

    return estados
########
def longitud_media_comentarios_por_estado(ovnis: list[ovnis]) -> dict[str, float]:
    '''
    longitud_media_comentarios_por_estado: Función que devuelve un diccionario en el que las claves son los estados 
    donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos
    observados en cada estado.
    '''
    '''
    estados = {}
    for ovni in ovnis:    # GPT !!
        estado = ovni.estado
        longitud_comentario = len(ovni.comentarios)
        # Si el estado no está en el diccionario, lo añadimos
        if estado not in estados:
            estados[estado] = []
        # Guardamos las longitudes de los comentarios para este estado
        estados[estado].append(longitud_comentario)
    # Calculamos la media para cada estado
    medias = {estado: sum(longitudes) / len(longitudes) for estado, longitudes in estados.items()}
    return medias'''
    
    estados={}
    for ovni in ovnis:
        estado=ovni.estado
        if estado not in estados:
            estados[estado]=[]
        len_comment = len(ovni.comentarios)
        estados[estado].append(len_comment)
    
    media_comments = {estado:sum(longitudes)/len(longitudes) for estado,longitudes in estados.items()}
    return media_comments    

                
def porc_avistamientos_por_forma(ovnis:list[ovnis])->dict[str,float]:
    '''
    porc_avistamientos_por_forma: Función que devuelve un diccionario en el que las claves son las formas de los avistamientos, 
    y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos.'''
    '''formas={}
    for ovni in ovnis:
        forma = ovni.forma
        if forma not in formas:
            formas[forma]=0.0
        formas[forma]=(((len(ovni)/len(ovnis))*100))
    return formas    '''
    dict_formas={}        
    formas=[ovni.forma for ovni in ovnis]
    count_formas = Counter(formas)
    #f"{number:.2f}")
    total_ovnis = len(ovnis)
    dict_formas={key :round((value/total_ovnis)*100,2) for key,value in count_formas.items()}
    return dict_formas
    
   # porcentajes = {forma: round((conteo / total_avistamientos) * 100, 1) for forma, conteo in formas.items()}

def avistamientos_mayor_duracion_por_estado(ovnis: list[ovnis], limite: int = 3) -> dict[str, list[ovnis]]:
    '''
    avistamientos_mayor_duracion_por_estado: Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor 
    duración observados en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos 
    de mayor duración. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará el límite que 
    por defecto tendrá el valor 3.
    '''
    # Diccionario para almacenar los resultados por estado
    estados = {}
    
    # Agrupar los avistamientos por estado
    for ovni in ovnis:
        estado = ovni.estado
        if estado not in estados:
            estados[estado] = []
        estados[estado].append(ovni)
    
    # Ordenar los avistamientos por duración en cada estado
    avistamientos_ordenados = {
        estado: sorted(avistamientos, key=lambda ovni: ovni.duracion, reverse=True)[:limite]
        for estado, avistamientos in estados.items()
    }
    
    return avistamientos_ordenados
  
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    