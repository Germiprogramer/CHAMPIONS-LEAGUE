#funcion para transformar el ranking según la regresion multilineal
def transform_rank(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif 3 <= x <= 4:
        return 4
    elif 5 <= x <= 8:
        return 8
    elif 9 <= x <= 16:
        return 16
    else:
        return 32