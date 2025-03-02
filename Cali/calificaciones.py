def check_nota(nota):
    result = nota
    if nota is None:
        result = 0
    return result


def nota_teoria(n1: float, n2: float) -> float:
    T1 = check_nota(n1)
    T2 = check_nota(n2)
    media = (T1 + T2) / 2
    return media


def nota_cuatrimestre(n1: float, n2: float, p: float) -> float:

    P = check_nota(p)

    NT = nota_teoria(n1, n2)
    if 4 <= NT:
        NC = 0.2 * NT + 0.8 * P
    else:
        NC = 0
    return NC


def nota_continua(C1, C2):

    cont = (C1 + C2) / 2

    if C1 < 4 or C2 < 4:
        print("cont es ", cont)
        cont = min(4, cont)
        return cont

    return cont


"""         
def nota_continua(T,P):
    C1 = nota_cuatrimestre(T[0], T[1], P[0])
    C2 = nota_cuatrimestre(T[2], T[3], P[1])
    cont = (C1 + C2) / 2
    
    if C1 < 4 or C2 < 4:
        print('cont es ',cont)
        cont=min(4,cont)
        return cont  
    
    return cont              
"""
