from centros import *
from coordenadas import *


coordenadas=[(36.135051666002795,-5.843455923196172),(36.189308321456515, -5.925475089376914),(3.08522545403537, -5.763703700430622)]

c1=Coordenadas(36.135051666002795,-5.843455923196172)
c2=Coordenadas(36.189308321456515, -5.925475089376914)
distancia = calcular_distancia(c1,c2)
distancia_euclidea = calcular_distancia_euclidea(c1,c2)
media_coord = calcular_media_coordenadas(coordenadas)

def main():
    print(distancia)
    print(distancia_euclidea)
    print(media_coord)

if __name__ == '__main__':
    main()



