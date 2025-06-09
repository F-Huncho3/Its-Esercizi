def sommaprimadiagonale(matrice:list[list]) ->int:

    somma = 0 

    for i in range(len(matrice)):

        somma += matrice[i][i]


    return somma


def sommasecondadiagonale(matrice:list[list]) ->int:

    somma = 0
    
    for i in range(len(matrice)):

        somma += matrice[i][len(matrice) - 1 - i ]

    return somma

