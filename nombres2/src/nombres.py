"""Año,Nombre,Frecuencia,Género
2002,ALEJANDRO,8020,Hombre
2002,PABLO,5799,Hombre
2002,DANIEL,5603,Hombre
2002,DAVID,5414,Hombre"""
# -*- coding: utf-8 -*-

from collections import namedtuple
import csv
import matplotlib.pyplot as plt

FrecuenciaNombre = namedtuple("FrecuenciaNombre", "anyo,nombre,frecuencia,genero")


# Reads a CSV file and returns a list of FrecuenciaNombre tuples
def leer_frecuencias_nombres(ruta: str) -> list[FrecuenciaNombre]:
    """recibe la ruta de un fichero CSV codificado en UTF-8,
    y devuelve una lista de tuplas de tipo FrecuenciaNombre(int, str, int, str)
    conteniendo todos los datos almacenados en el fichero."""
    res = []
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            anyo = int(linea[0])
            nombre = str(linea[1])
            frecuencia = int(linea[2])
            genero = str(linea[3])
            cadena = FrecuenciaNombre(anyo, nombre, frecuencia, genero)
            res.append(cadena)
    return res

# Filters FrecuenciaNombre records by gender
def filtrar_por_genero(frecuencias: list[FrecuenciaNombre], genero: str) -> list[FrecuenciaNombre]: 
    '''recibe una lista de tuplas de tipo FrecuenciaNombre y 
    un género de tipo str, y devuelve una lista de tuplas de tipo FrecuenciaNombre 
    con los registros del género recibido como parámetro.'''
    res = []
    for registro in frecuencias:
        if registro.genero == genero or genero is None:
            res.append(registro)
    return res        

# Gets all unique names for a given gender (or all if gender is None)
def calcular_nombres(frecuencias: list[FrecuenciaNombre], genero: str = None) -> set[str]:
    '''calcular_nombres: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
    y devuelve un conjunto {str} con los nombres del género recibido como parámetro.'''
    registros = filtrar_por_genero(frecuencias, genero)
    nombres = set()
    for registro in registros:
        nombres.add(registro.nombre)
    return nombres    

# Filters records by a specific year and gender
def filtra_genero_anyo(frecuencias: list[FrecuenciaNombre], anyo: int, genero: str = None) -> list[FrecuenciaNombre]:
    registro_genero = filtrar_por_genero(frecuencias, genero)
    registro_anyo_genero = []
    for registro in registro_genero:
        if registro.anyo == anyo:
            registro_anyo_genero.append(registro)
    registro_nombre_frecuencia = []
    for registro in registro_anyo_genero:
        registro_nombre_frecuencia.append((registro.nombre, registro.frecuencia))
    return registro_nombre_frecuencia            

# Gets the top N most frequent names for a specific year and gender
def calcular_top_nombres_de_año(frecuencias: list[FrecuenciaNombre], anyo: int, genero: str, limite) -> list[str, int]:
    '''calcular_top_nombres_de_año: recibe una lista de tuplas de tipo FrecuenciaNombre, un año de tipo int, 
    un número límite de tipo int y un género de tipo str, y devuelve una lista de tuplas (nombre, frecuencia) de tipo (str, int).'''    
    registro_nombre_frec = filtra_genero_anyo(frecuencias, anyo, genero)
    top_nombres = sorted(registro_nombre_frec, key=lambda x: x[1], reverse=True)
    return top_nombres[:limite]

# Gets names that appear in both genders
def calcular_nombres_ambos_generos(frecuencias: list[FrecuenciaNombre]) -> set[str]:
    '''calcular_nombres_ambos_generos: recibe una lista de tuplas de tipo FrecuenciaNombre, 
    y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.'''
    nombres_comun = set()
    hombres = {registro.nombre for registro in frecuencias if registro.genero == "Hombre"}
    mujeres = {registro.nombre for registro in frecuencias if registro.genero == "Mujer"}
    for registro in frecuencias: 
        if registro.nombre in (hombres & mujeres):
            nombres_comun.add(registro.nombre)
    return nombres_comun        

# Gets names with more than one word for a specific gender (or all if gender is None)
def calcular_nombres_compuestos(frecuencias: list[FrecuenciaNombre], genero: str = None) -> set[str]:
    '''calcular_nombres_compuestos: recibe una lista de tuplas de tipo FrecuenciaNombre y 
    un género de tipo str, y devuelve un conjunto {str} con los nombres que contienen más de una palabra.'''            
    nombres_compuestos = set()    
    registro_genero = filtrar_por_genero(frecuencias, genero)
    nombres = {registro.nombre for registro in registro_genero}
    for nombre in nombres:
        palabras = nombre.split()
        if len(palabras) > 1:
            nombres_compuestos.add(nombre)
    return nombres_compuestos        

# Filters records by a range of years
def filtra_nombres_anyos(frecuencias: list[FrecuenciaNombre], anyoin: int, anyofin: int) -> list[FrecuenciaNombre]:
    registro_nombres = []
    for registro in frecuencias:
        if registro.anyo in range(anyoin, anyofin):
            registro_nombres.append(registro)
    return registro_nombres

# Calculates the average frequency of a name across a range of years
def calcular_frecuencia_media_nombre_años(frecuencias: list[FrecuenciaNombre], nombre: str, anyoin: int, anyofin: int) -> float:
    '''calcula la frecuencia media de un nombre en un rango de años dado.'''
    registro_nombres = []
    registro_anyos = filtra_nombres_anyos(frecuencias, anyoin, anyofin)
    for registro in registro_anyos:
        if registro.nombre == nombre:
            registro_nombres.append((registro.nombre, registro.frecuencia))
    frecs = [e[1] for e in registro_nombres]
    media = sum(frecs) / len(frecs) if frecs else 0
    return media          

# Gets the most frequent name for a specific year and gender
def calcular_nombre_mas_frecuente_año_genero(frecuencias: list[FrecuenciaNombre], anyo: int, genero: str = None) -> list[str]:
    '''devuelve el nombre más frecuente en un año y género dados.'''          
    registro_nombres = filtra_genero_anyo(frecuencias, anyo, genero)
    if registro_nombres:
        max_frec = max(registro_nombres, key=lambda x: x[1])
        return max_frec if max_frec else None
    else:
        return None

# Gets the year with the highest frequency for a given name
def calcular_año_mas_frecuencia_nombre(frecuencias: list[FrecuenciaNombre], nombre: str) -> int:   
    '''devuelve el año con mayor frecuencia de un nombre dado.'''
    registro_nombres = []
    for registro in frecuencias:
        if registro.nombre == nombre:
            registro_nombres.append((registro.nombre, registro.anyo, registro.frecuencia))    
    if registro_nombres:        
        registro_frecuencia = max(registro_nombres, key=lambda x: x[2])
        return registro_frecuencia[0], registro_frecuencia[1]   
    else:
        return None 

# Filters records by gender and decade
def filtra_genero_decada(frecuencias: list[FrecuenciaNombre], genero: str, decada: int) -> list[FrecuenciaNombre]:
    anyoin = decada
    anyofin = decada + 10
    registro_genero = filtrar_por_genero(frecuencias, genero)
    registro_anyos = filtra_nombres_anyos(registro_genero, anyoin, anyofin)
    return registro_anyos

# Gets the top N most frequent names for a given gender and decade
def calcular_nombres_mas_frecuentes(frecuencias: list[FrecuenciaNombre], genero: str, decada: int, n: int = 5) -> list[str]:    
    '''devuelve los N nombres más frecuentes de un género en una década dada.'''
    registro_genero_decada = filtra_genero_decada(frecuencias, genero, decada)
    nombres = sorted(registro_genero_decada, key=lambda x: x.frecuencia, reverse=True)
    nombres_frecuentes = [nombre.nombre for nombre in nombres]
    return nombres_frecuentes[:n]


def calcular_año_frecuencia_por_nombre(frecuencias : list [FrecuenciaNombre],genero:str)->dict[str,list[tuple[int,int]]]:
    
    '''
    calcular_año_frecuencia_por_nombre: recibe una lista de tuplas de tipo FrecuenciaNombre y 
    un género, y devuelve un diccionario en el que las claves son los nombres y los valores una lista de tuplas (año, frecuencia) 
    para cada nombre del género dado como parámetro.'''
    registro_genero = filtrar_por_genero(frecuencias,genero)
    registro_dict={}
    
    for registro in registro_genero:
        if registro.nombre not in registro_dict:
            registro_dict[registro.nombre] = []
            registro_dict[registro.nombre].append((registro.anyo,registro.frecuencia))
    
    return registro_dict   

def calcular_nombre_mas_frecuente_por_año(frecuencias : list[FrecuenciaNombre],genero:str)->list[tuple[int,str,int]]:#anyo,nombre,frecuencia
    '''calcular_nombre_mas_frecuente_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
    y devuelve una lista de tuplas (año, nombre, frecuencia) de tipo (int, str, int) ordenada por año con el nombre más frecuente de cada año. 
    El género puede ser Hombre o Mujer.'''
    
    registro_genero = filtrar_por_genero(frecuencias,genero)
    registro_dic ={}
    
    for registro in registro_genero:
        if registro.anyo not in registro_dic:
            registro_dic[registro.anyo]=[]
        registro_dic[registro.anyo].append(registro)    
    
    res=[]
    for clave,valor in registro_dic.items():
        max_frecuentes = max(valor ,key = lambda x : x.frecuencia)
        res.append((clave, max_frecuentes.nombre , max_frecuentes.frecuencia))
        
    res.sort(key = lambda x:x[0])

    return res 

def filtra_por_nombre (frecuencias:list[FrecuenciaNombre],nombre:str)->list[FrecuenciaNombre]: #devuelve anyo,frec de un nombre dado 
    res=[]
    for registro in frecuencias:
        if registro.nombre == nombre :
            res.append((registro.anyo,registro.frecuencia))
    return res         
            
def calcular_frecuencia_por_año(frecuencias : list[FrecuenciaNombre], nombre:str)->list[tuple[int,int]]: #anyo , frecuencia 

    '''
    calcular_frecuencia_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de tipo str, 
    y devuelve una lista de tuplas (año, frecuencia) de tipo (int, int) ordenada por año con la frecuencia del nombre en cada año. 
    En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias.'''
    
    registro_nombre = filtra_por_nombre(frecuencias,nombre)
    registro_dic={}
    for anyo,frecuencia in registro_nombre:
        if anyo not in registro_dic:
            registro_dic[anyo]=0
        registro_dic[anyo]+=frecuencia
                
        anyos_ordenados = sorted(registro_dic.items()) 
    return anyos_ordenados
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calcular_nombres_ambos_generos1(frecuencias: list[FrecuenciaNombre]) -> set[str]:
    '''
    calcular_nombres_ambos_generos: recibe una lista de tuplas de tipo FrecuenciaNombre, 
    y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
    '''
    # Crear conjuntos de nombres por género
    hombres = {registro.nombre for registro in frecuencias if registro.genero == "Hombre"}
    mujeres = {registro.nombre for registro in frecuencias if registro.genero == "Mujer"}
    
    # Intersección de ambos conjuntos para encontrar nombres comunes
    nombres_comun = hombres & mujeres
    
    return nombres_comun
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
def mostrar_evolucion_por_año(frecuencias:list[FrecuenciaNombre],nombre:str):
    '''
    mostrar_evolucion_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de tipo str, y 
    genera un gráfico con la evolución de la frecuencia del nombre a lo largo de los años(Figura 1). 
    Se usarán las siguientes instrucciones para generar la gráfica, donde años y frecuencias se extraen del resultado de la función calcular_frecuencia_por_año.:
    
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()
    '''
    datos_por_año = calcular_frecuencia_por_año(frecuencias, nombre)
    
    # Separar años y frecuencias
    años = [dato[0] for dato in datos_por_año]
    frecuencias = [dato[1] for dato in datos_por_año]
    
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show() 





