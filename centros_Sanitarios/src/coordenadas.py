'''
calcular_distancia: recibe dos coordenadas de tipo Coordenadas(float, float) y devuelve un float que representa la distancia euclídea entre esas dos coordenadas.

calcular_media_coordenadas: recibe una lista de Coordenadas(float, float) y devuelve una tupla de tipo Coordenadas(float, float) 
cuya latitud es la media de las latitudes de la lista y cuya longitud es la media de las longitudes de la lista.
'''
from math import sqrt
from collections import namedtuple 
Coordenadas = namedtuple('Coordenadas',['latitud', 'longitud'])

'''
NOMBRE;LOCALIDAD;LATITUD;LONGITUD;ESTADO;NUM_CAMAS;TIENE_ACCESO_DISCAPACITADOS;TIENE_UCI
CONSULTORIO ZAHARA DE LOS ATUNES; BARBATE; 36.135051666002795; -5.843455923196172; BUENO; 0; true; false
CENTRO DE SALUD BARBATE; BARBATE; 36.189308321456515; -5.925475089376914; BUENO; 0; true; false
'''

def calcular_distancia(Coordenadas1:Coordenadas,Coordenadas2:Coordenadas)->float:
    '''
    recibe dos coordenadas de tipo Coordenadas(float, float) y devuelve un float que representa la distancia euclídea entre esas dos coordenadas.'''
    '''
    latitud = (Coordenadas1[0]-Coordenadas2[0])
    longitud = (Coordenadas1[1]-Coordenadas2[1])
    
    return sqrt(latitud**2 + longitud**2)'''
    
    latitud = Coordenadas1.latitud - Coordenadas2.latitud 
    longitud = Coordenadas1.longitud - Coordenadas2.longitud
    
    distancia = sqrt(latitud**2 + longitud**2)
    return distancia

def calcular_distancia_euclidea(c1:Coordenadas,c2:Coordenadas)->float:
    '''CALCULA DISTANCIA ENTRE 2 COORDS '''
    longitud = c1.longitud-c2.longitud
    latitud = c1.latitud-c2.latitud
    distancia = sqrt (latitud**2 + longitud**2)
    return distancia


def calcular_media_coordenadas(coord:list[Coordenadas])->list[Coordenadas]:
    
    '''
    calcular_media_coordenadas: recibe una lista de Coordenadas(float, float) y devuelve una tupla de tipo Coordenadas(float, float) 
    cuya latitud es la media de las latitudes de la lista y cuya longitud es la media de las longitudes de la lista.'''

    latitudes = [x[0] for x in coord]
    longitudes = [x[1] for x in coord]
    
    latitud_media = sum(latitudes)/len(latitudes)
    longitud_media = sum(longitudes)/len(longitudes)
    
    return Coordenadas(latitud_media,longitud_media) 



