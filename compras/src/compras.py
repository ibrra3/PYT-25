'''dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra
62745110Y,Carrefour,Almeria,01/01/2019 04:43,01/01/2019 06:19,175.71
94320158X,Aldi,Malaga,01/01/2019 14:53,01/01/2019 15:55,70.04
55993608Q,Lidl,Sevilla,01/01/2019 20:09,01/01/2019 20:19,43.09'''

import csv 
from collections import namedtuple , Counter
from datetime import datetime


Compras = namedtuple("Compras","dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra")

def lee_compras (ruta:str)->list[Compras]:
    
    with open(ruta , encoding='utf-8') as f:
        res=[]
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            dni=str(linea[0]) #dni <- linea[0]
            supermercado=str(linea[1])
            provincia=str(linea[2])
            fecha_llegada=datetime.strptime(linea[3],"%d/%m/%Y %H:%M")
            fecha_salida=datetime.strptime(linea[4],"%d/%m/%Y %H:%M")
            total_compra=float(linea[5])
            cadena = Compras(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra)     
            res.append(cadena)
    return res    

'''compra_maxima_minima_provincia: recibe una lista de tuplas de tipo Compra y una provincia. 
Devuelve una tupla que contiene el importe máximo y el mínimo de las compras que se han realizado en la provincia dada como parámetro. 
Si la provincia toma el valor None, se devuelve una tupla con el importe máximo y el mínimo calculados a partir de todas las compras. (1 punto)'''

def compra_maxima_minima_provincia(Compras:list[Compras],provincia:str)->tuple[float,float]:
    lista=[]
    total=[]
    for compra in Compras:
        if compra.provincia==provincia or  provincia is None:
            lista.append(compra)
        elif provincia is None:
            lista.append(Compras)    
            
    for compra in lista:     
        total.append(compra.total_compra)      
          
    if not total:
        return (0, 0)    
    
    maximo=max(total)
    minimo=min(total)
    
    return (maximo,minimo)  


def hora_menos_afluencia (Compras:list[Compras])->tuple[str,int]:
    '''hora_menos_afluencia: recibe una lista de tuplas de tipo Compra y 
    devuelve una tupla con la hora en la que llegan menos clientes 
    y el número de clientes que llegan a dicha hora. (1,5 puntos)'''   
 
    lista=[]
    horas=[]
    for compra in Compras:
        lista.append(compra.fecha_llegada)
        horas.append(datetime.strptime(fecha, "%d/%m/%Y %H:%M").hour)

    for fecha in lista:
        datetime.strptime(fecha,"%d/%m/%Y %H:%M").hour  
        horas.append(fecha)
        
    contador=Counter(horas)
    hora_max = contador.most_common(1)  
    clientes = contador.most_common[0]          
    return (hora_max,clientes)