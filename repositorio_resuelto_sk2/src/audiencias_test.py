from audiencias import *

ruta = "data\GH.csv"
ediciones = {2}


lectura = lee_Audiencia(ruta)
num_ediciones = calcular_ediciones(lectura)
filtra_audiencias = filtra_audiencias(lectura, ediciones)

share_edition = porcentaje_edicion(lectura)

porcentajes = media_porcentaje_por_audiencia(lectura, 1)


def main():
    print(lectura)


if __name__ == "__main__":
    main()
