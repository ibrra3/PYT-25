import csv
from collections import namedtuple
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple("RegistroPoblacion", "pais, codigo, ano, censo")
# Finland,FIN,1967,4605744


def lee_poblaciones(ruta):
    with open(ruta, encoding="utf-8") as f:
        poblaciones = []
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            pais = linea[0]
            codigo = linea[1]
            ano = linea[2]
            censo = linea[3]
            tupla = RegistroPoblacion(pais, codigo, ano, censo)
            poblaciones.append(tupla)
        return poblaciones


# RegistroPoblacion(pais='Zimbabwe', codigo='ZWE', año='2016', censo='16150362')]
def calcula_paises(poblaciones):
    paises = set()
    for registro in poblaciones:
        paises.add(registro.pais)
    return sorted(paises)


def filtra_por_pais(poblaciones, nombre_code):
    filtrado_paises = []
    for registro in poblaciones:
        if nombre_code == registro.pais or nombre_code == registro.codigo:
            filtrado_paises.append((registro.ano, registro.censo))
    return sorted(filtrado_paises)


def filtra_pais_ano(poblaciones, ano, paises):
    # te da el pais y el ano , le devuelves el pais y el censo para el ano indicado
    filter = []
    for registro in poblaciones:
        if registro.ano == ano and registro.pais in paises:
            filter.append((registro.pais, registro.censo))
    return filter


def muestra_evolucion(poblaciones, nombre_code):
    poblaciones_evo = []
    anos1 = []
    censo1 = []
    titulo = f"la evolucion de la poblacion en {nombre_code} es "

    for registro in poblaciones:
        if registro.codigo == nombre_code or registro.pais == nombre_code:
            anos1.append(int(registro.ano))
            censo1.append(float(registro.censo))

    plt.title(titulo)
    plt.plot(anos1, censo1)
    plt.show()


def muestra_evolucion2(poblaciones, nombre_code):
    poblaciones_evo = []
    anos1 = []
    censo1 = []
    titulo = f"la evolucion de la poblacion en {nombre_code} es "

    for registro in poblaciones:
        if registro.codigo == nombre_code or registro.pais == nombre_code:
            poblaciones_evo.append(registro)
    for poblacion in poblaciones_evo:
        anos1.append(int(poblacion.ano))
        censo1.append(float(poblacion.censo))
    plt.title(titulo)
    plt.plot(anos1, censo1)
    plt.show()


def selecciona(data: list[tuple[int, int]], indice: int):
    res = []
    for x in data:
        res.append(x[indice])
    return res


def muestra_comparativa(poblacion, ano, lista_paises):

    titulo = "Poblaciones en anyo " + str(ano)
    datos = filtra_pais_ano(poblacion, ano, lista_paises)
    paises = selecciona(sorted(datos), 0)
    lista_habitantes = selecciona(sorted(datos), 1)
    plt.title(titulo)
    plt.bar(paises, lista_habitantes)
    plt.show()
