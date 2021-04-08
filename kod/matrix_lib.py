import numpy as np

# macierz kwadratowa, to taka gdzie wysokość
# oraz wszystkie szerokości są takie same
def is_matrix_square(M):
    h = len(M)
    w = len(M[0])
    # sprawdź czy pierwszy wiersz i wysokość się zgadzają
    if (h != w): return False
    # sprawdź czy wszystkie wiersze mają tę samą szerokość
    for line in M:
        if (w != len(line)): return False
    # jak jest ok, to zwróc True
    return True


# Macierz dominująca/zbieżna to macierz, której wartości
# bezwzględne elementów na głównej przekątnej są
# większe od sumy wartości bezwzględnych
# pozostałych elementów w wierszach
def is_matrix_weakly_convergent(M):
    # dla każdej linii macierzy
    weak = 0
    for i in range(len(M)):
        # policz sumę wartości bezwzględnych
        # z wyłączeniem wartości na przekątnej
        sum = 0
        for j in range(len(M[i])):
            if (i == j): continue
            sum += abs(M[i][j])
        if (abs(M[i][i]) >= sum):
            weak +=1
    if (weak == len(M)): return True
    return False

def is_matrix_positivly_specified(M):
    return np.all(np.linalg.eigvals(M) > 0)
    