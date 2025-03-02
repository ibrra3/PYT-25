from centros import *
from coordenadas import *
ruta = "data\centrosSanitarios.csv"
coords=Coordenadas(36.33232154964611, -6.091332824370154)
umbral = 10.0


CENTROS=leer_centros(ruta)
#read=lectura(ruta)
centros_acceso=calcular_total_camas_centros_accesibles(CENTROS)
centros_uci = centros_con_uci(CENTROS)
distancia_centro = calcula_distancia_coords(CENTROS,coords)

centros_cercanos = obtener_centros_con_uci_cercanos_a(CENTROS,coords,umbral)

def main():
    '''print("-"*100)
    print(distancia_centro)
    print("-"*100)
    print(centros_cercanos)'''
    #print(centros_uci)
    #print(len(centros_uci))
    #print(distancia_centro)
    print(centros_cercanos)
    print(len(centros_cercanos))
if __name__=='__main__':
    main()    