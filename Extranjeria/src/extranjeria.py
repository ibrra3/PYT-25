# THIS IS AN ATTACK BY TEKKERA . SK-2 

'''
DISTRITO,SECCION,BARRIO,PAIS_NACIMIENTO,HOMBRES,MUJERES
01,001,SANTA CATALINA,ALEMANIA,8,6
01,001,SANTA CATALINA,ARGELIA,0,1
'''

from collections import namedtuple
from csv import reader
from collections import Counter
RegistroExtranjeria = namedtuple('RegistroExtranjeria','distrito,seccion,barrio,pais,hombres,mujeres')


def lee_datos_extranjeria (ruta:str)->list[RegistroExtranjeria]:
    
    '''lee_datos_extranjeria(ruta_fichero): recibe la ruta del fichero CSV, devolviendo una lista de tuplas de tipo RegistroExtranjeria 
    con toda la información contenida en el fichero.'''

    with open (ruta, encoding='utf-8') as fitchero :
        lector = reader(fitchero,delimiter=',')
        next(lector)
        res=[]
        for distrito,seccion,barrio,pais,hombres,mujeres in lector:
            distrito = int(distrito)
            seccion = int(seccion)
            barrio = str(barrio)
            pais = str(pais)
            hombres = int(hombres)
            mujeres = int (mujeres)
            cadena = RegistroExtranjeria(distrito,seccion,barrio,pais,hombres,mujeres)
            res.append(cadena)
        return res     

def numero_nacionalidades_distintas(datos:list[RegistroExtranjeria])->int:
    '''
    numero_nacionalidades_distintas(registros): recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve el número de nacionalidades distintas presentes en los registros de la lista recibida como parámetro.'''
    #res = set()
    #resultado = set(registro.pais for registro in datos)
    resultado2 = {registro.pais for registro in datos}
    #for registro in datos : 
        #res.add(registro.pais)
    return len(resultado2)    


def secciones_distritos_con_extranjeros_nacionalidades(datos:RegistroExtranjeria , paises :set[str])->list[tuple[str,int]]:
    '''
    secciones_distritos_con_extranjeros_nacionalidades(registros, paises): recibe una lista de tuplas de tipo RegistroExtranjeria y 
    un conjunto de cadenas con nombres de países, y devuelve una lista de tuplas (distrito, seccion) con los distritos y secciones 
    en los que hay extranjeros del conjunto de paises dado como parámetro. La lista de tuplas devuelta estará ordenada por distrito.'''
    
    '''
    res=[]
    for registro in datos : 
        if registro.pais in paises:
            res.append((registro.distrito,registro.seccion))
    return sorted(res,key= lambda x:x[0])             
    '''
    res = [(registro.distrito,registro.seccion) for registro in datos if registro.pais in paises]
    return sorted(res , key= lambda x:x[0])
    

def extranjeros_por_pais(datos:list[RegistroExtranjeria],pais:str)->int:
    hombres=[]
    mujeres=[]
    
    for registro in datos:
        if registro.pais == pais:
            hombres.append(registro.hombres)
            mujeres.append(registro.mujeres)
    return sum(hombres)+sum(mujeres)
    
def total_extranjeros_por_pais(datos : list[RegistroExtranjeria])->dict[str:int]:
    
    '''total_extranjeros_por_pais(registros): recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve 
    un diccionario de tipo {str:int} en el que las claves son los países y
    los valores son el número total de extranjeros (tanto hombres como mujeres) de cada país.'''
    #dicc[pais:num extranjeros]
    paises = {}
    for registro in datos:
        if registro.pais not in paises:
            paises[registro.pais]=0
        paises[registro.pais]+=registro.hombres + registro.mujeres    
           
    return paises

    
def top_n_extranjeria(datos:RegistroExtranjeria,n:int=3)->list[tuple[str,int]]:    
    '''
    top_n_extranjeria(registros, n=3): recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve una lista de tuplas (pais, numero_extranjeros) con los n países de los 
    que hay más población extranjera en los registros pasados como parámetros.'''
    #from collections import Counter   !!! 
    paises_extranjeros = total_extranjeros_por_pais(datos)
    #paises_extranjeros_sorted =sorted(paises_extranjeros,key= lambda x:x[1],reverse=True)
    contador = Counter(paises_extranjeros)
    return contador.most_common(n)
    #return contador
    #print(help(Counter))
    

def barrio_mas_multicultural(datos:list[RegistroExtranjeria])->str:    
    '''
    barrio_mas_multicultural(registros): recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve el nombre del barrio en el que hay un mayor número de países de procedencia distintos.'''
    barrios={}   # es un diccionario no set 
    for registro in datos:
        if registro.barrio not in barrios:
           barrios[registro.barrio]=set() # initialize an empty set for registro.barrio
        barrios[registro.barrio].add(registro.pais)   
    dicc = {barrio:len(paises) for barrio,paises in barrios.items()}  
    contador = Counter(dicc)   
    return contador.most_common(1)[0][0]   
           

def barrio_con_mas_extranjeros(datos:list[RegistroExtranjeria], tipo:str=None)->str:
    '''
    barrio_con_mas_extranjeros(registros, tipo=None): recibe una lista de tuplas de tipo RegistroExtranjeria 
    y devuelve el nombre del barrio en el que hay un mayor número de extranjeros, bien sea en total 
    (tanto hombres como mujeres) si tipo tiene el valor None, bien sea de hombres si tipo es 'Hombres',
    o de mujeres si tipo es 'Mujeres'.'''
    # el barrio con mas extranjeros 
    
    

'''pais_mas_representado_por_distrito(registros): recibe una lista de tuplas de tipo RegistroExtranjeria y 
devuelve un diccionario de tipo {str:str} en el que las claves son los distritos y 
los valores los países de los que hay más extranjeros residentes en cada distrito.'''           