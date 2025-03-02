'''
APELLIDOS Y NOMBRE;CALLE;NÚMERO;FECHA DE ADQUISICIÓN;METROS;PRECIO;MEJORAS
AGUILAR CABALLERO, CARLOS;HALCÓN;30;10/10/2018;138,29;395488;BUHARDILLA-13379-30/11/2019*PLACAS
SOLARES-13502-04/04/2023*PISCINA-8945-29/10/2020*GARAJE-13177-20/01/2023
ALONSO GARCÍA, AGUSTÍN;PALOMA;5;01/03/2013;190,69;395379;PISCINA-10277-11/09/2014
ALONSO NAVARRO, BEATRIZ;PALOMA;11;17/09/2005;156,62;437807;GARAJE-11783-04/03/2007'''
from csv import reader
#                                   NUNCA HE VISTO UN VS CODE QUE NO GUARDE CODIGO AUTOMATICAMENTE ! 
from typing import NamedTuple
from datetime import datetime,date
Mejora =NamedTuple("Mejora",[("denominacion", str),("coste", int),
("fecha", date)])

Vivienda = NamedTuple("Vivienda",
[("propietario", str),
("calle", str),
("fecha_adquisicion", date),
("numero", int),
("metros",float),
("precio",int),
("mejoras", list[Mejora])])

#La cadena de formato para parsear las fechas es "%d/%m/%Y"

def parsea_mejoras(mejoras_str:str) -> list[Mejora]:
    '''
    dada una cadena de texto con las mejoras separadas por *, devuelva una lista de tipo Mejora'''
#BUHARDILLA-13379-30/11/2019*PLACAS SOLARES-13502-04/04/2023*PISCINA-8945-29/10/2020*GARAJE-13177-20/01/2023    
    res=[]
    cada_mejora = mejoras_str.split('*')
    mejora_trozos = (str(cada_mejora)).split('-')
    for linea in mejora_trozos:
        #mejora = linea.split('-')
        denominacion = linea[0]
        coste =linea[1]
        fecha=linea[2]
        res.append(Mejora(denominacion,coste,fecha))
    return res 




#APELLIDOS Y NOMBRE;CALLE;NÚMERO;FECHA DE ADQUISICIÓN;METROS;PRECIO;MEJORAS
#-------------------------------------------------------------------------------------------------------------------  

def lee_viviendas(ruta: str) -> list[Vivienda]:
    '''
    Recibe la ruta de un fichero CSV y devuelve una lista de tuplas de tipo Vivienda conteniendo
    todos los datos almacenados en el fichero''' 
    res=[]
    with open (ruta, encoding='utf-8') as fichero:
        lector = reader(fichero,delimiter=';') 
        next(lector)
       #APELLIDOS Y NOMBRE;CALLE;NÚMERO;FECHA DE ADQUISICIÓN;METROS;PRECIO;MEJORAS
        #AGUILAR CABALLERO, CARLOS;HALCÓN;30;10/10/2018;138,29;395488;BUHARDILLA-13379-30/11/2019*PLACAS
        for nombre,calle,numero,fecha,metros,precio,mejoras in lector:
            propietario=str(nombre.strip())
            calle = str(calle.strip())
            fecha_adquisicion = fecha
            fecha_adquisicion = datetime.strptime(fecha_adquisicion,"%d/%m/%Y")
            numero = int(numero)
            metros = float(metros)
            precio = int(precio)
            mejoras = parsea_mejoras(mejoras)
            cadena = Vivienda(propietario,calle,fecha_adquisicion,numero,metros,precio,mejoras)
            res.append(cadena)
        return res     

#-------------------------------------------------------------------------------------------------------------------  

def filtra_viviendas(viviendas: list[Vivienda], par_impar: str)->list[Vivienda]:
    res=[]
    if par_impar == "par":
        res = [registro for registro in viviendas if registro.numero %2==0]
    else:
        res =[registro for registro in viviendas if registro.numero %2==1]

    return res 

def total_mejoras_por_calle (viviendas: list[Vivienda], par_impar: str) ->dict[str,int]:
    '''Devuelve un diccionario que hace corresponder cada calle con el número total de mejoras de
    las viviendas de número par o impar de esa calle, según sea el valor del parámetro
    par_impar. El parámetro par_impar puede tomar los valores "par" o "impar".'''

    zonas = filtra_viviendas(viviendas,par_impar)
    calles ={}
    for zona in zonas:
        calle = zona.calle
        if calle not in calles:
            calles[calle] = 0
        calles[calle]=(len(zona.mejoras))
    return calles    


#-------------------------------------------------------------------------------------------------------------------  

def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) ->tuple[str,str,int,int,str]:

    '''
    Devuelve una tupla con información de la vivienda que menos días tardó en hacer una mejora
    desde que fue adquirida.'''

    '''
     La tupla contendrá el propietario, la calle, el número, el número de
    días transcurridos entre la adquisición de la vivienda y la primera mejora, y la denominación
    de esa mejora.'''
    for registro in viviendas:
        fechas = sorted(registro)
    return None









