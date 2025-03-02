# Segundo Control Teoría FP Curso 24-25

### Apellidos, Nombre: ___________________________________________

### DNI: _____________________________


## Contexto

La empresa Festi World S.A. pone a su disposición un dataset con algunos datos de los festivales de música que organiza. La compañía necesita que se exploten estos datos y, para ello, le solicita una serie de funciones para extraer información relevante. Los datos que le suministra en un fichero CSV son los siguientes:

- **Nombre del festival**.
- **Fecha de comienzo del festival**.
- **Fecha de finalización del festival**.
- **Estado del festival**, que puede tomar los valores `PLANIFICADO`, `CELEBRADO` o `CANCELADO`, en función del estado actual del festival.
- **Precio de la entrada**, que puede tomar valores decimales.
- **Entradas vendidas**: número de entradas vendidas.
- **Artistas**, que es un listado de artistas que actúan en el festival y de ellos tenemos:
  - **Nombre**
  - **Hora de actuación**
  - **Caché**: cantidad en miles de euros que cobra el artista por actuar.
- **Top**, que toma como valor "sí" o "no" en función de si el festival es considerado top mundial o no.

Una línea del fichero que nos proporcionan tiene el siguiente aspecto:

```console
Tomorrowland,2024-07-19,2024-07-21,PLANIFICADO,280.99,70000,David Guetta_20:00_700-Tiësto_21:30_750-Calvin Harris_23:00_800,sí
```

e indica que:

- El festival Tomorrowland se celebra desde el 19 de julio de 2024 al 21 de julio de 2024, y su estado actual es PLANIFICADO. La entrada tiene un precio de 280.99€ y se han vendido un total de 70.000 entradas. En este festival actúan David Guetta a las 20:00 cobrando 700 mil euros, después actúa Tiësto a las 21:00 cobrando 750 mil, y Calvin Harris a las 23:00 cobrando 800 mil euros. Por último, este festival sí está considerado como uno de los tops.

Para facilitar los encargos de la empresa se han dividido sus peticiones en diferentes ejercicios, que tiene a continuación.

### Ejercicios

Para la realización de los ejercicios se usarán las siguientes definiciones de `namedtuple` y su uso será obligatorio:

```python
from typing import NamedTuple, List, Dict, Tuple, Optional, Set
 
Artista = NamedTuple("Artista",     
                        [("nombre", str), 
                        ("hora_comienzo", time), 
                        ("cache", int)])

Festival = NamedTuple("Festival", 
                        [("nombre", str),
                        ("fecha_comienzo", date),
                        ("fecha_fin", date),
                        ("estado", str),                      
                        ("precio", float),
                        ("entradas_vendidas", int),
                        ("artistas", List[Artista]),
                        ("top", bool)
                    ])
```

Como ejemplo, para el festival anterior obtendremos la siguiente tupla. Fíjese con detalle en el tipo de cada uno de los campos:

```text
Festival(nombre='Tomorrowland', fecha_comienzo=datetime.date(2024, 7, 19), fecha_fin=datetime.date(2024, 7, 21), estado='PLANIFICADO', precio=280.99, entradas_vendidas=70000, artistas=[Artista(nombre='David Guetta', hora_comienzo=datetime.time(20, 0), cache=700), Artista(nombre='Tiësto', hora_comienzo=datetime.time(21, 30), cache=750), Artista(nombre='Calvin Harris', hora_comienzo=datetime.time(23, 0), cache=800)], top=True)
```

Se pide realizar las siguientes funciones:

1. `anyos_cancelaciones`: recibe una lista de tuplas de tipo `Festival` y devuelve una lista con los anyos de los festivales que se cancelaron. **(3 puntos)**

```python
def anyos_cancelaciones(festivales: List[Festival]) -> List[int]
```

2. `top_n_anyo_con_mas_cancelaciones`: recibe una lista de tuplas de tipo `Festival` y un número `n` y devuelve
una lista de n tuplas con los años con mayor número de cancelaciones y sus correspondientes números de cancelaciones.  **(3 puntos)**

```python
def top_n_anyo_con_mas_cancelaciones(festivales: List[Festival], n:int) -> List[Tuple[int, int]]
```

3. `anyo_mayor_beneficio_medio`: recibe una lista de tuplas de tipo `Festival` y devuelve una tupla con el anyo con un mayor beneficio medio en los festivales celebrados y su correspondiente beneficio medio. Es decir, cada festival `CELEBRADO` tiene un beneficio que se calcula a partir de las entradas vendidas menos el caché de los artistas. Esta función debe calcular el beneficio medio que se ha obtenido cada anyo y devolver aquél cuyo beneficio haya sido el mayor. **Nota**: Si hubiera algún festival que se celebra entre dos anyos, se imputará el anyo en el que comienza. **(4 puntos)**

```python
def anyo_mayor_beneficio_medio(festivales: List[Festival]) -> Tuple[int, float]
```
