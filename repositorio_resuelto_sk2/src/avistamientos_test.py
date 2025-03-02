from avistamientos import *

ruta = "data\ovnis.csv"
from datetime import date

lectura = lee_ovnis(ruta)

fecha = date(2006, 4, 5)
estados = {"in", "pa", "nm"}
ovni_fecha = numero_avistamientos_fecha(lectura, fecha)

estados_formas = formas_estados(lectura, estados)

duracion_estado = duracion_total(lectura, "nm")
c1 = Coordenadas(latitud=36.135051666002795, longitud=-5.843455923196172)
c2 = Coordenadas(latitud=36.189308321456515, longitud=-5.925475089376914)
c3 = Coordenadas(39.1722222, -120.1377778)
c4 = Coordenadas(38.9636111, -84.0808333)
# Calculate distance
radio = distancia_coords(c3, c4)
distancia = 1

ovnis_cercanos = avistamientos_cercanos_ubicacion(lectura, c3, distancia)

forma = "circle"
ovni_forma_max_duracion = avistamiento_mayor_duracion(lectura, forma)

ovni_cerca_coment_duracion = avistamiento_cercano_mayor_duracion(lectura, c3, distancia)
fechain=date(2000,1,1)
fechafin=date(2000,2,1)
ovnis_fechas = avistamientos_fechas(lectura,fechain,fechafin)

x=saca_comentario(lectura)

coment_largo = comentario_mas_largo(lectura,2001,"green")

media_entre_ovnis = media_dias_entre_avistamientos(lectura,1990)
x2 = cuenta_ovnis_anyo(lectura , 1990)

ovni_fecha = avistamientos_por_fecha(lectura)

formas_mes =formas_por_mes(lectura)
formas_mes_2 =fromas_mes(lectura)

ovnis_ano =numero_avistamientos_por_año(lectura)

ovnis_mes=num_avistamientos_por_mes(lectura)
ovnis_mes2=num_avistamientos_por_mes2(lectura)

x3=formas_por_mes2(lectura)

hora_max_ovnis=hora_mas_avistamientos(lectura)

most_coords = coordenadas_mas_avistamientos(lectura)

comentario_estado =longitud_media_comentarios_por_estado(lectura)

media_comment = longitud_media_comentarios_por_estado(lectura)

porc_formas =porc_avistamientos_por_forma(lectura)


def main():
    print("STARTED")
    print("#" * 500)
    print(porc_formas)
    print()
    print("FINISHED")
    #print(len(lectura))


if __name__ == "__main__":
    main()
