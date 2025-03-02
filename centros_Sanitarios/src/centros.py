'''
/src: Contiene los diferentes módulos de Python que conforman el proyecto.
centros.py: Contiene funciones para explotar los datos de los centros sanitarios.
centros_test.py: Contiene funciones de test para probar las funciones del módulo centros.py. En este módulo está el main.
coordenadas.py: Contiene funciones para trabajar con el tipo Coordenadas.
coordenadas_test.py: Contiene funciones de test para probar las funciones del módulo coordenadas.py.
mapas.py: Contiene funciones para crear un mapa y representar puntos en él. Requiere tener instalada la librería folium.
/data: Contiene el dataset o datasets del proyecto
centrosSanitarios.csv: Archivo con los datos de población de diversos paises o agrupaciones de paises en distintos años.
'''
'''
NOMBRE;LOCALIDAD;LATITUD;LONGITUD;ESTADO;NUM_CAMAS;TIENE_ACCESO_DISCAPACITADOS;TIENE_UCI
CONSULTORIO ZAHARA DE LOS ATUNES; BARBATE; 36.135051666002795; -5.843455923196172; BUENO; 0; true; false
'''
print("hi")

#THIS IS AN SK OPERATION - TEKKERA LIMITED. 
#SK-2


'''from collections import namedtuple 

person = namedtuple ("person","name,age,height,sex,colour")
p=person("john",15,150,"male","black")

'''
from coordenadas import *
from collections import namedtuple
from csv import reader
#CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool)

CentroSanitario = namedtuple ("CentroSanitario","NOMBRE,LOCALIDAD,Coordenadas,ESTADO,NUM_CAMAS,TIENE_ACCESO_DISCAPACITADOS,TIENE_UCI")

def lectura(ruta:str)->list[CentroSanitario]:
    '''
    leer_centros: recibe la ruta de un fichero CSV codificado en UTF-8, y 
    devuelve una lista de tuplas de tipo CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool)
    conteniendo todos los datos almacenados en el fichero.'''
    cadena=[]   
    with open(ruta, encoding='utf-8') as f:
        lector = reader(f,delimiter=';')
        next(lector)
        
        for linea in lector:
            NOMBRE=str(linea[0])
            LOCALIDAD=str(linea[1])
            latitud =float(linea[2])
            longitud=float(linea[3])
            ESTADO=str(linea[4])
            NUM_CAMAS=int(linea[5])
            TIENE_ACCESO_DISCAPACITADOS=bool(linea[6])
            TIENE_UCI=bool(linea[7])
            cadena.append(CentroSanitario(NOMBRE,LOCALIDAD,Coordenadas(latitud,longitud),ESTADO,NUM_CAMAS,TIENE_ACCESO_DISCAPACITADOS,TIENE_UCI))    
    return cadena        

def leer_centros(ruta:str)->list[CentroSanitario]:
    res=[]
    with open (ruta,encoding='utf-8') as f:
        lector = reader(f,delimiter=';')
        next(lector)
        for NOMBRE,LOCALIDAD,LATITUD,LONGITUD,ESTADO,NUM_CAMAS,TIENE_ACCESO_DISCAPACITADOS,TIENE_UCI in lector:
            NOMBRE=str(NOMBRE)
            LOCALIDAD=str(LOCALIDAD)
            LATITUD=float(LATITUD)
            LONGITUD=float(LONGITUD)
            ESTADO=ESTADO 
            NUM_CAMAS=int(NUM_CAMAS)
            TIENE_ACCESO_DISCAPACITADOS=TIENE_ACCESO_DISCAPACITADOS.strip().lower() == 'true'
            TIENE_UCI=TIENE_UCI.strip().lower() == 'true'
            cadena=CentroSanitario(NOMBRE,LOCALIDAD,Coordenadas(LATITUD,LONGITUD),ESTADO,NUM_CAMAS,TIENE_ACCESO_DISCAPACITADOS,TIENE_UCI)
            res.append(cadena) 
    return res


def calcular_total_camas_centros_accesibles(centros:list[CentroSanitario])->int:
    '''
    calcular_total_camas_centros_accesibles: recibe una lista de tuplas de tipo CentroSanitario y produce como salida un entero correspondiente 
    al número total de camas de los centros sanitarios accesibles para discapacitados.'''
    
    '''
    res=0
    for centro in centros:
        if centro.TIENE_ACCESO_DISCAPACITADOS is True:
            res+=centro.NUM_CAMAS
    return res  
    '''       
    centros_accesibles = filter(lambda c:c.TIENE_ACCESO_DISCAPACITADOS,centros)
    camas = map(lambda c : c.NUM_CAMAS,centros_accesibles)
    return sum(camas)

def centros_con_uci (centros:list[CentroSanitario])->list[CentroSanitario]:
    '''centros_uci=[]
    for centro in centros:
        if centro.TIENE_UCI:
            centros_uci.append(centro)
    return centros_uci
    '''
    return [centro for centro in centros if centro.TIENE_UCI]

           
def calcula_distancia_coords(centros:list[CentroSanitario],coords:Coordenadas)->list[CentroSanitario]:
    centro_uci=centros_con_uci(centros)
    '''USSLESS FUNCTION
    CALCULA LA DISTANCIA DE TODOS LOS CENTROS CON UCI A UNA COORDENADA DADA'''
    distancia = [calcular_distancia_euclidea(centro.Coordenadas,coords) for centro in centro_uci]    
    return distancia
    

def obtener_centros_con_uci_cercanos_a(centros:list[CentroSanitario],coords:Coordenadas,umbral:float)->list[tuple[str,str,Coordenadas]]:
    '''
    obtener_centros_con_uci_cercanos_a: recibe una lista de tuplas de tipo CentroSanitario; una tupla de tipo Coordenadas, que representa un punto; y un float, 
    que representa un umbral de distancia. Produce como salida una lista de tuplas (str, str, Coordenadas(float, float)) con el nombre, del centro, la localidad y 
    la ubicacion de los centros con uci situados a una distancia de las coordenadas dadas como parámetro menor o igual que el umbral dado. Observe la Figura 3 para'''
    
    #centro_cercano=[]
    centros_cercanos = filter(lambda centro : calcular_distancia_euclidea(centro.Coordenadas,coords)<=umbral , centros)
    
    return [(centro.NOMBRE, centro.LOCALIDAD, centro.Coordenadas) for centro in centros_cercanos if centro.TIENE_UCI]
   
    
    