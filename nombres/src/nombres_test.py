from nombres import *

s = "data\lasfrec.csv"
genero = 'Mujer'
nombre='SERGIO'
listaFrecuencias = lee_frecuencias_nombres(s)        #...................LECTURA 
frecuenciasGenero = filtrar_por_genero(listaFrecuencias,genero)#...................FILTRA POR GENERO 
nombres = calcular_nombres(listaFrecuencias,genero) #................... FILTRA POR GENERO -> SET
top_nombre = top_nombre_ano(listaFrecuencias,2016,12,genero) #................... NOMBRE MAS FRECUENTE DE UN AÑO 

nombres_gen_ano=f'\nfiltra genero ano {filtra_nombres_genero_ano(listaFrecuencias,2016,genero)}\n' #................... FILTRA NOMBRE POR GENERO Y AÑO 
SIGN_OUT = fuck_you()
nombres_repetidos =f'\n{calcular_nombres_ambos_generos(listaFrecuencias)}\n'  #................... NOMBRES PARA MUJER Y HOMBRE 
names= f'\nnames {sacar_nombres(listaFrecuencias)}' #................... SACA LOS NOMBRES DE UNA LISTA TIPO FRECUENCIAS NOMBRE

nombres_compuestos = f'\nnombres_compuestos {calcular_nombres_compuestos(listaFrecuencias,genero)}\n'
nombres_compuestos2 =f'\nnombres_compuestos2 {calcular_nombres_compuestos2(listaFrecuencias,genero)}\n'

frec_media = calcular_frecuencia_media_nombre_años(listaFrecuencias,nombre,2003,2010)

x2=calcular_nombre_mas_frecuente_año_genero(listaFrecuencias,2002,genero)
x3=calcular_año_mas_frecuencia_nombre(listaFrecuencias,nombre)
x4 = calcular_nombres_mas_frecuentes(listaFrecuencias,genero,2005,5)
def main():
    #print(SIGN_OUT)
    #print(listaFrecuencias)
    #print(frecuenciasGenero)
    #print(nombres)
    #print(nombres_gen_ano)
    #print(top_nombre)
    #print(names)
    #print(nombres_repetidos)
    #print(nombres_compuestos)
    #print(nombres_compuestos2)
    #print(frec_media)
    #print(x2)
    print(x4)
    
if __name__ == "__main__":
    main()
