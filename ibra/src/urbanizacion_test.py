
from urbanizacion import *


ruta = 'data\\urbanizacion.csv'

mejoraa = "BUHARDILLA-13379-30/11/2019*PLACAS SOLARES-13502-04/04/2023*PISCINA-8945-29/10/2020*GARAJE-13177-20/01/2023"


test_mejora = parsea_mejoras(mejoraa)
lectura = lee_viviendas(ruta)
parimpar="impar"
total_mejoras = total_mejoras_por_calle(lectura,parimpar)

filtra = filtra_viviendas(lectura,"impar")

def main():
    #print(lectura)
    print(total_mejoras)

if __name__== "__main__":
    main()    










