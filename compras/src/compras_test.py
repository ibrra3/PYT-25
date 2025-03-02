from  compras import *


ruta='data\compras.csv'
lectura = lee_compras(ruta)
#-------------------------------------------------------------------
provincia="Huelva"
total = compra_maxima_minima_provincia(lectura,provincia)
#-------------------------------------------------------------------
hora=hora_menos_afluencia(lectura)


def main():
    #print(lectura)
    #print(total)
    print(hora)
    
if __name__ == "__main__":
    main()    