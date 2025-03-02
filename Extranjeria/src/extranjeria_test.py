from extranjeria import * 
ruta = 'data\extranjeriaSevilla.csv'
paises = ("ITALIA")
pais=("MARRUECOS")
lectura = lee_datos_extranjeria(ruta)
nacionalidades = numero_nacionalidades_distintas(lectura)
distritos_secciones = secciones_distritos_con_extranjeros_nacionalidades(lectura,paises)
num_por_pais = extranjeros_por_pais(lectura,pais)
paises_extranjeros = total_extranjeros_por_pais((lectura))

paises_mas_comunes = top_n_extranjeria(lectura,3)

barrio_cultural = barrio_mas_multicultural(lectura)
import time
def main():
    #print("STARTED")
    #print(barrio_cultural)
    #print(paises_mas_comunes)
    #print("ENDED")
    start = time.time()
    print(paises_extranjeros)
    print("Execution time:", time.time() - start, "seconds")
if __name__ =='__main__':
    main()    