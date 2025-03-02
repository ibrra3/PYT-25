from nombres import *
# -*- coding: utf-8 -*-

ruta = "data\las_frecuencias.csv"
genero = 'Hombre'
anyo=1990
limite=10
anyoin=2003
anyofin=2016
nombre='IKER'
decada=2003
frecuencias = leer_frecuencias_nombres(ruta)
frec_genero = filtrar_por_genero(frecuencias,genero)
calcula_nombres = calcular_nombres(frecuencias,genero)

frec_genero_anyo=filtra_genero_anyo(frecuencias,anyo,genero)
top_nombres = calcular_top_nombres_de_año(frecuencias,anyo,genero,limite)

nombre_comun = calcular_nombres_ambos_generos(frecuencias)
nombres_compuestos = calcular_nombres_compuestos(frecuencias,genero)
filtra_rango_anyos = filtra_nombres_anyos(frecuencias,anyoin,anyofin)
calcula_media_nombres = calcular_frecuencia_media_nombre_años(frecuencias,nombre,anyoin,anyofin)

nombre_mas_frecuente = calcular_nombre_mas_frecuente_año_genero(frecuencias,anyo,genero)
anyo_max_frec = calcular_año_mas_frecuencia_nombre(frecuencias,nombre)

filtra_decada = filtra_genero_decada(frecuencias,genero,decada)
filtra_nombres_decada =calcular_nombres_mas_frecuentes(frecuencias,genero,decada,7)

registro_dict = calcular_año_frecuencia_por_nombre(frecuencias,genero)

nombres_frec_anyo = calcular_nombre_mas_frecuente_por_año(frecuencias,genero)
frec_anyo = calcular_frecuencia_por_año(frecuencias,nombre)
plot = mostrar_evolucion_por_año(frecuencias,nombre)
def main():
    #print("hi")
    #print(lee_frecuencias)
    #print(frec_genero)
    #print(calcula_nombres)
    #print(frec_genero_anyo)
    print(plot)
if __name__=='__main__':
    main()