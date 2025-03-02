from ovnis import *
from datetime import datetime
def test_numero_avistamientos_fecha(lista, fecha):
    print("Hay ", numero_avistamientos_fecha(lista, fecha), " avistamientos en el listado")

def test_lee_ovnis(lista)->None:
    print(len(lista), " registros en el fichero")
    print(lista[0], " es el primer registro")
    print(lista[-1], " es el último registro")

def test_avistamientos_por_fecha(lista)->None:
    diccionario = avistamientos_por_fecha(lista)
    print(len(diccionario[datetime(2012, 12, 3).date()]))

def test_avistamientos_por_fecha_2(lista)->None:
    diccionario = avistamientos_por_fecha_2(lista)
    print(len(diccionario[datetime(2012, 12, 3).date()])) 

def test_avistamiento_mayor_duracion(lista)->None:
    print(avistamiento_mayor_duracion(lista, 'light'))
    print(avistamiento_mayor_duracion_2(lista, 'light'))

def test_hora_mas_avistamientos(lista):
    print(horas_mas_avistamientos(lista))

def main()->None:
    lista_ovnis = lee_ovnis("data/ovnis.csv")
    #test_lee_ovnis(lista_ovnis)
    #test_numero_avistamientos_fecha(lista_ovnis, datetime(2012, 12, 3).date())
    #test_avistamientos_por_fecha(lista_ovnis)
    #test_avistamientos_por_fecha_2(lista_ovnis)
    #dicc = dict()
    #print(dicc['mateo'])
    #dicc['mateo'] = 'pregunta'
    #print(dicc['mateo'])
    #test_avistamiento_mayor_duracion(lista_ovnis)
    #test_hora_mas_avistamientos(lista_ovnis)
    #print(coordenadas_mas_avistamientos(lista_ovnis))
    print(media_dias_entre_avistamientos(lista_ovnis, 1999))

if __name__ == "__main__":
    main()