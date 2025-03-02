from repositorios import*
ruta = "data\\repositorios.csv"
lectura = lee_repositorios(ruta)

total_commits =total_commits_por_anyo(lectura)
from datetime import datetime
from typing import NamedTuple, List, Set, Tuple, Dict, Optional
import datetime
rep= Repositorio(nombre='ProjectX', propietario='user123', 
                 lenguajes={'Python', 'JavaScript'}, privado=True,
                 commits=[Commit(id='b789101', mensaje='Initial commit', 
                   fecha_hora=datetime.datetime(2023, 10, 6, 12, 0)),Commit(id='c567891', mensaje='Added main functionality',
                       fecha_hora=datetime.datetime(2023, 10, 6, 13, 0))])
tasa = calcular_tasa_crecimiento(rep)


mejores_tasas = n_mejores_repos_por_tasa_crecimiento(lectura,3)


def main():
    print(lectura[0])

if __name__ == "__main__":
    main()    
    
    