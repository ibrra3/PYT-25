from datetime import datetime
from csv import reader
from collections import defaultdict, namedtuple, Counter
from math import floor
from tipos_auxiliares import Coordenadas

Ovni = namedtuple('Ovni', 'fecha, ciudad, estado, forma, duracion, comentarios, coordenadas')

def lee_ovnis(nombre_fichero:str)->list[str]:
    result = []
    with open(nombre_fichero, encoding="utf-8") as fichero:
        lector = reader(fichero)
        #hay cabecera así que...
        next(lector)
        #datetime,city,state,shape,duration,comments,latitude,longitude
        #07/04/2011 22:00,muncie,in,light,240,((HOAX??))...,
        # 40.1933333,-85.3863889
        for trozos in lector:
            fecha = datetime.strptime(trozos[0], "%m/%d/%Y %H:%M")
            city = trozos[1].strip()
            state = trozos[2].strip()
            shape = trozos[3].strip()
            duration = int(trozos[4])
            comments = trozos[5].strip()
            latitude = float(trozos[6])
            longitude = float(trozos[7])
            result.append(Ovni(fecha, city, 
                           state, shape, duration, comments, Coordenadas(latitude, longitude)))
    return result

def numero_avistamientos_fecha(avistamientos:list[Ovni], objetivo:datetime.date)->int:
    ''': 
    Función que obtiene el número total de avistamientos 
    que se han producido en una fecha determinada, 
    dada por su día, mes y año. 
    Se contarán, por tanto, los avistamientos que hayan tenido lugar 
    a cualquier hora del día. 
    La función recibe una lista de namedtuple de tipo Avistamiento, 
    y una fecha de tipo datetime.date.'''
    result = []
    for r in avistamientos:
        if  r.fecha.date() == objetivo:
            result.append(r)
    return len(result)

def formas_estados(avistamientos: list[Ovni], estados:set[str])->int:
    '''formas_estados: Función que obtiene el número de formas distintas 
    que presentaron los avistamientos observados en uno o varios estados. 
    La función recibe una lista de namedtuple de tipo Avistamiento, y un conjunto de estados de tipo str.
        
    result = []
    for r in avistamientos:
        if r.estado in estados:
            result.append(r.forma)
    return len(set(result))'''
    result = filter (lambda a: a.estado in estados, avistamientos)
    formas = map(lambda a: a.forma, result)
    return len(set(formas))

def duracion_total(avistamientos: list[Ovni], estado:str)->int:
    '''
    duracion_total: Función que devuelve la duración total en segundos de los avistamientos que se han observado en un estado. 
    La función recibe una lista de namedtuple de tipo Avistamiento, y un estado de tipo str.
    '''
    filtro = [r for r in avistamientos if r.estado == estado]
    
    #filtro = []
    #for r in avistamientos:
    #    if r.estado == estado:
    #        filtro.append(r)
    
    #filtro = filter(lambda a: a.estado == estado, avistamientos)
    
    transformacion = [r.duracion for r in filtro]
    
    #transformacion = []
    #for r in filtro:
    #    transformacion.append(r.duracion)
    
    #transformacion = map(lambda a: a.duracion, filtro)
    
    return sum(transformacion)



'''distancia: Función que calcula la distancia euclidea entre dos coordenadas. La función recibe dos tuplas de tipo (float, float).
avistamientos_cercanos_ubicacion: Función que calcula un conjunto con los avistamientos cercanos a una ubicacion dada. Concretamente, vamos a obtener los avistamientos que se encuentren dentro de un determinado radio de distancia de la ubicación. La función recibe una lista de namedtuple de tipo Avistamiento, una ubicación que será una tupla de tipo (float, float), y una distancia de tipo float.'''

def avistamiento_mayor_duracion(avistamientos: list[Ovni], forma:str)-> Ovni:
    '''avistamiento_mayor_duracion: Función que obtiene el avistamiento de mayor 
    duración de entre todos los avistamientos que tienen una forma determinada. 
    La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo str.'''
    filtrado = filter(lambda a: a.forma == forma, avistamientos)
    return max(filtrado, key=lambda a: a.duracion)


def media_dias_entre_avistamientos(avistamientos: list[Ovni], anyo:int=None)->float:
    '''media_dias_entre_avistamientos: Función que devuelve la media de días transcurridos 
    entre dos avistamientos consecutivos en el tiempo. 
    La función permite hacer el cálculo para todos los avistamientos, 
    o solo para los de un año concreto. 
    La función recibe una lista de namedtuple de tipo Avistamiento y un año de tipo int.'''
    avistamientos_anyo = filter(lambda a: a.fecha.year == anyo, avistamientos)
    avistamientos_ordenados = sorted(avistamientos_anyo, key=lambda a: a.fecha)
    dias_iniciales = map(lambda a: a.fecha, avistamientos_ordenados[:-1])
    dias_finales = map(lambda a: a.fecha, avistamientos_ordenados[1:]) 
    pares = list(zip(dias_iniciales, dias_finales))
    pares = list(map(lambda par: (par[1] - par[0]).days, pares))
    return sum(pares)/len(pares)


'''
avistamiento_cercano_mayor_duracion: Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada; es decir, la distancia entre las coordenadas del avistamiento y las coordenadas que se pasan como parámetro de entrada debe ser menor al radio que también aparece como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios). La función recibe una lista de namedtuple de tipo Avistamiento, una coordenada que será una tupla de tipo (float, float), y una distancia de tipo float.
avistamientos_fechas: Función que devuelve una lista con los avistamientos observados entre una fecha inicial y una fecha final, 
ambas inclusive. La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. Si la fecha inicial es None, se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es None, se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son None, se devolverá la lista de avistamientos completa. La función recibe una lista de namedtuple de tipo Avistamiento, y dos fechas de tipo datetime.date: una como principio del intervalo y otra como final. Las fechas recibidas como parámetro tendrán como valor por defecto None.'''

def avistamientos_por_fecha(avistamientos: list[Ovni])-> dict[datetime.date, list[Ovni]]:
    '''avistamientos_por_fecha: Función que crea un 
    diccionario que relaciona las fechas con los avistamientos 
    observados en dichas fechas. Es decir, un diccionario cuyas claves 
    son las fechas y cuyos valores son los conjuntos de avistamientos observados 
    en cada fecha. La función recibe una lista de namedtuple de tipo Avistamiento.'''
    result = dict()

    for ufo in avistamientos:
        clave = ufo.fecha.date()
        #valor = [ufo]
        if clave in  result:
            #listado_antiguo = result[clave]
            #valor = valor + listado_antiguo
            #result[clave] = valor
            result[clave].append(ufo)
        else:
            #result[clave]=valor
            result[clave] = [ufo]

    return result

def avistamientos_por_fecha_2(avistamientos: list[Ovni])-> dict[datetime.date, list[Ovni]]:
    '''avistamientos_por_fecha: Función que crea un 
    diccionario que relaciona las fechas con los avistamientos 
    observados en dichas fechas. Es decir, un diccionario cuyas claves 
    son las fechas y cuyos valores son los conjuntos de avistamientos observados 
    en cada fecha. La función recibe una lista de namedtuple de tipo Avistamiento.'''
    result = defaultdict(list)

    for ufo in avistamientos:
        clave = ufo.fecha.date()
        result[clave].append(ufo)

    return result

def formas_por_mes(avistamientos:list[Ovni])-> dict[str, set[str]]: 
    '''Función que devuelve un diccionario que indexa las distintas formas de avistamientos por 
    los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las formas distintas 
    observadas en dicho mes. La función recibe una lista de namedtuple de tipo Avistamiento.'''
    result = dict()
    for ufo in avistamientos:
        clave = ufo.fecha.date().month
        if clave in result:
            result[clave].add(ufo.forma)
        else:
            valor = set()
            result[clave] = valor
            result[clave].add(ufo.forma)
    return result 

def formas_por_mes_2(avistamientos:list[Ovni])-> dict[str, set[str]]: 
    '''Función que devuelve un diccionario que indexa las distintas formas de avistamientos por 
    los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las formas distintas 
    observadas en dicho mes. La función recibe una lista de namedtuple de tipo Avistamiento.'''
    result = defaultdict(set)
    for ufo in avistamientos:
        clave = ufo.fecha.date().month
        result[clave].add(ufo.forma)
    return result

def numero_avistamientos_por_dia(avistamientos: list[Ovni])-> dict[datetime.date, int]:
    '''result = {}
    for ufo in avistamientos:
        clave = ufo.fecha.date()
        if clave in result:
            result[clave] += 1
        else:
            result[clave] = 1
    return result'''
    fechas = map(lambda a: a.fecha.date(), avistamientos)
    contador = Counter(fechas)
    return contador

def numero_avistamientos_por_dia_default(avistamientos: list[Ovni])-> dict[datetime.date, int]:
    result = defaultdict(int)
    for ufo in avistamientos:
        clave = ufo.fecha.date()
        result[clave] += 1
    return result


def formas_por_mes(avistamientos:list[Ovni])-> dict[str, set[str]]:
    result = defaultdict(set)
    meses = ['Enero', 'Febrero', 'Marzo']
    for ufo in avistamientos:
        clave = meses[ufo.fecha.date().month]
        result[clave].add(ufo.forma)
    return result

def avistamiento_mayor_duracion(avistamientos: list[Ovni], forma:str)-> Ovni:
    '''avistamiento_mayor_duracion: Función que obtiene el avistamiento de mayor 
    duración de entre todos los avistamientos que tienen una forma determinada.
    La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo str.
    '''
    result = None
    for ufo in avistamientos:
        if ufo.forma == forma and (result is None or ufo.duracion > result.duracion):
                result = ufo
    return result

def avistamiento_mayor_duracion_2(avistamientos: list[Ovni], forma:str)-> Ovni:
    '''avistamiento_mayor_duracion: Función que obtiene el avistamiento de mayor 
    duración de entre todos los avistamientos que tienen una forma determinada.
    La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo str.
    
    result = []
    for av in avistamientos:
        if av.forma==forma:
            result.append(av)'''
    result = filter(lambda av: av.forma == forma, avistamientos)
    return max(result, key=lambda a:a.duracion)

'''
avistamiento_cercano_mayor_duracion: Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada;
 es decir, la distancia entre las coordenadas del avistamiento y las coordenadas 
 que se pasan como parámetro de entrada debe ser menor al radio que también aparece
   como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios). 
   La función recibe una lista de namedtuple de tipo Avistamiento, una coordenada que será una
     tupla de tipo (float, float), y una distancia de tipo float.'''

def checkFecha(potencial: datetime.date, real: datetime.date)->datetime.date:
    result = real
    if real is None:
        result = potencial
    return result

def avistamientos_fechas(avistamientos: list[Ovni], inicial:datetime.date=None, fin: datetime.date=None)->list[Ovni]:
    ''': Función que devuelve una lista 
    con los avistamientos observados entre una fecha inicial y una fecha final, 
    ambas inclusive. 
    La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. 
    
    Si la fecha inicial es None, se devolverán todos los avistamientos
    desde el más antiguo hasta la fecha final. 
    Si la fecha final es None, se devolverán todos los avistamientos desde la 
    fecha inicial hasta el más reciente. Si ambas fechas son None, 
    se devolverá la lista de avistamientos completa. 

    La función recibe una lista de namedtuple de tipo Avistamiento, 
    y dos fechas de tipo datetime.date: una como principio del intervalo y otra como final.
    Las fechas recibidas como parámetro tendrán como valor por defecto None.'''
    inicial = checkFecha(min(avistamientos).fecha, inicial)
    fin = checkFecha(max(avistamientos).fecha, fin)
    result = []
    for av in avistamientos:
        if inicial <=  av.fecha <= fin:
            result.append(av)
    return sorted(result, reverse=True)


def hora_mas_avistamientos(avistamientos: list[Ovni])->int:
    '''* **hora_mas_avistamientos**: Función que devuelve la hora del día (de 0 a 23) 
    en la que se han observado un mayor número de avistamientos.'''
    horas = map(lambda a:a.fecha.hour, avistamientos)
    c = Counter(horas)
    lista_maximos:list[tuple[int, int]] = c.most_common(1) #
    tupla:tuple[int, int] = lista_maximos[0]
    return tupla[0]
    #return c.most_common(1)[0][0]

def horas_mas_avistamientos(avistamientos: list[Ovni])->int:
    '''* **horas_mas_avistamientos**: Función que devuelve las horas del día 
    (de 0 a 23) 
    en la que se han observado un mayor número de avistamientos.'''
    horas = map(lambda a:a.fecha.hour, avistamientos)
    c = Counter(horas)
    frecuencia_maxima = c.most_common(1)[0][1]
    return list(filter(lambda tupla: tupla[1]==frecuencia_maxima, c.items()))

def comentario_mas_largo(avistamientos: list[Ovni], anyo:int, palabra:str)->Ovni:
    '''comentario_mas_largo: Función que devuelve el avistamiento con el comentario más largo, 
    de entre todos los avistamientos observados en un año dado y cuyo comentario incluye una palabra concreta. 
    La función recibe una lista de namedtuple de tipo Avistamiento, un año de tipo int, y una palabra de tipo str.
    result = None
    for a in avistamientos:
        if a.fecha.year == anyo and palabra in a.comentarios:
            if result is None or len(a.comentarios) > len(result.comentarios):
                result = a
    return result
    '''
    filtrado = filter(lambda a: a.fecha.year == anyo and palabra in a.comentarios, avistamientos)
    return max(filtrado, key=lambda a: len(a.comentarios))

def anyo_mas_avistamientos_forma(avistamientos: list[Ovni], forma:str)->int:
    '''
    **año_mas_avistamientos_forma**: Función que devuelve el año en 
    el que se han observado más avistamientos de una forma dada. 
    La función recibe una lista de namedtuple de tipo Avistamiento y 
    la forma a tener en cuenta que será de tipo _str_.
    '''
    ovnis_formas = filter(lambda a: a.forma == forma, avistamientos)
    #ovnis_por_anyo = defaultdict(list)
    #for ovni in ovnis_formas:
    #    ovnis_por_anyo[ovni.fecha.year].append(ovni)
    #return max(ovnis_por_anyo.items(), key=lambda t: len(t[1]))[0]
    #return max(ovnis_por_anyo.keys(), key=lambda k: len(ovnis_por_anyo[k]))
    anyos = map(lambda a: a.fecha.year, ovnis_formas)
    result = Counter(anyos)
    listado_mas_frecuentes = result.most_common(1)
    mas_frecuente = listado_mas_frecuentes[0]
    anyo_mas_frecuente = mas_frecuente[0]
    return anyo_mas_frecuente

def longitud_media_comentarios_por_estado(avistamientos: list[Ovni])->dict[str, float]: 
    '''
    **longitud_media_comentarios_por_estado**: 
    Función que devuelve un diccionario en el que las claves son los estados donde se producen 
    los avistamientos, y los valores son la longitud media de los comentarios 
    de los avistamientos observados en cada estado.
    
    result = defaultdict(int)
    contador = Counter(map(lambda a: a.estado, avistamientos))
    for a in avistamientos:
        result[a.estado] += len(a.comentarios)/contador[a.estado]
    return result'''
    
    #agregación
    result = defaultdict(int)
    for a in avistamientos:
        result[a.estado].append(a)
    #transformación
    #result = {k:sum(map(lambda a: len(a.comentarios), v))/len(v) for k,v in result.items()}
    nuevo_result = dict()
    for estado, listado_avistamientos in result.items():
        longitudes_texto = map(lambda a: len(a.comentarios), listado_avistamientos)
        longitud_media = sum(longitudes_texto)/len(longitudes_texto)
        nuevo_result[estado] = longitud_media
    return nuevo_result
        

def estado_con_suma_top_n_duraciones_mas_largas(avistamientos: list[Ovni], n:int = 3)-> str:
    #agregación
    result = defaultdict(list)
    for a in avistamientos:
        result[a.estado].append(a)
    #transformación 1
    for estado, listado_avistamientos in result.items():
        result[estado] = sorted(listado_avistamientos, key=lambda a: a.duracion, reverse=True)[:n]
    #transformación 2
    for estado, listado_avistamientos in result.items():
        result[estado] = sum(map(lambda a: a.duracion, listado_avistamientos))
    
    return max(result.items(), key=lambda t: t[1])[0]

'''
* **avistamientos_por_fecha**: Función que crea un diccionario que relaciona las fechas 
con los avistamientos observados en dichas fechas. 
Es decir, un diccionario cuyas claves son las fechas y cuyos valores 
son los conjuntos de avistamientos observados en cada fecha. 
La función recibe una lista de namedtuple de tipo Avistamiento.

* **formas_por_mes**: Función que devuelve un diccionario que 
indexa las distintas formas de avistamientos por los nombres de los meses
 en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas
   las formas distintas observadas en dicho mes. La función recibe una lista de namedtuple 
   de tipo Avistamiento.

* **numero_avistamientos_por_año**: Función que crea un diccionario que relaciona 
cada año con el número de avistamientos observados en dicho año. 
Es decir, un diccionario cuyas claves son los años y cuyos valores son el número 
de avistamientos observados en cada año. La función recibe una lista de namedtuple de tipo Avistamiento.

* **num_avistamientos_por_mes**: Función que devuelve el número de avistamientos observados 
en cada mes del año. Usar como claves los nombres de los doce meses con la inicial en mayúsculas:

```meses = ["Enero", "Febrero", "Marzo",
            "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", 
            "Octubre", "Noviembre", "Diciembre"]
```
* 
* **porc_avistamientos_por_forma**: Función que devuelve un 
diccionario en el que las claves son las formas de los avistamientos, y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos.
* **avistamientos_mayor_duracion_por_estado**: Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor duración observados en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos de mayor duración. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará el límite que por defecto tendrá el valor 3.
* 
* **estados_mas_avistamientos**: Función que devuelve una lista con el nombre y el número de avistamientos de los estados con mayor número de avistamientos, ordenados de mayor a menor número de avistamientos. Si no se indica nada, se obtendrán los cinco estados con más avistamientos. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará el límite que por defecto tendrá el valor 3.
* 
* **avistamiento_mas_reciente_estado**: Función que devuelve un diccionario que relaciona cada estado con la fecha del último avistamiento observado en el estado.
'''

def coordenadas_mas_avistamientos(avistamientos: list[Ovni])->Coordenadas:
    '''**coordenadas_mas_avistamientos**: Función que devuelve las coordenadas enteras 
    que se corresponden con la zona donde más avistamientos se han observado. 
    Por ejemplo, si hay avistamientos en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), 
    la zona con más avistamientos corresponde a las coordenadas enteras (40, -85) con 2 avistamientos.'''
    frecuencias = defaultdict(lambda:0) #defaultdict(int)
    for a in avistamientos:
        key = Coordenadas(floor(a.coordenadas.latitud), floor(a.coordenadas.longitud))
        frecuencias[key] += 1
    return max(frecuencias.items(), key = lambda t:t[1])

def anyo_con_mayor_duracion_total_avistamientos(avistamientos: list[Ovni])->int:
    '''devuelve el año en el que la duración total de avistamientos fue mayor'''
    result = defaultdict(int)
    for tupla in avistamientos:
        result[tupla.fecha.year] += tupla.duracion
    return max(result.items(), key = lambda a: a[1])[0]


def top_n_avistamientos_mas_largos_por_anyo(avistamientos: list[Ovni], n:int = 3)->dict[int, list[Ovni]]:
    '''Devuelve un diccionario con los n avistamientos con mayor duracion por año.'''
    #TODO: Próximo día
    pass

'''**duracion_total_avistamientos_año**: Función que devuelve un diccionario que relaciona cada año con la suma de las duraciones de todos los avistamientos observados durante ese año en un estado dado. La función recibe una lista de namedtuple de tipo Avistamiento y el estado a tener en cuenta que será de tipo _str_.'''