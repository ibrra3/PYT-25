from poblacion import *

poblacions = lee_poblaciones("data\population.csv")
paises_filter = calcula_paises(poblacions)
filtrado_pais = filtra_por_pais(poblacions, "Spain")

set_paises = {"Spain", "Portugal", "France", "Mexico", "China"}

filter_pais_ano = filtra_pais_ano(poblacions, "2016", set_paises)
evolucion = muestra_evolucion(poblacions, "Spain")
evolucion2 = muestra_evolucion2(poblacions, "Spain")


list_paises2 = ["Spain", "Portugal", "France", "Mexico", "China"]
comparativa = muestra_comparativa(poblacions, "2016", list_paises2)


def main():

    print("\n", poblacions, "\n")
    print("-----paises---------")
    print("\n", paises_filter, "\n")
    print("filterar por pais")
    print("\n", filtrado_pais, "\n")
    print("\nfilterar pais ano:\n", filter_pais_ano)
    print(evolucion)
    print(evolucion2)
    print()
    print("comparativa paises")
    print(comparativa)


if __name__ == "__main__":
    main()
