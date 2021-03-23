import numpy as np
import matrix_lib as lib

# szuka na podstawie tego
# https://pl.wikipedia.org/wiki/Metoda_Gaussa-Seidla#Uk%C5%82ad_trzech_r%C3%B3wna%C5%84_liniowych
# search(), to wykonanie jednej iteracji
# rozrysowane jak działa kod jest w pliku
# "komentarz do funkcji search.png"
def search(M, out, X):
    for i in range(len(M)):
        sum = 0
        for j in range(len(M)):
            if (i == j): continue
            sum -= M[i][j]*X[j]
        sum += out[i]
        sum /= M[i][i]
        X[i] = sum
    return X


# sprawdza czy maksymalna względna zmiana składowej
# przybliżonego rozwiązania nie przekracza eps
def error_A(prev_xs, xs, eps=None):
    '''
    prev_xs - poprzedni wynik\n
    xs      - obecny wynik\n
    eps     - jeżeli nie podany funkcja zwróci zmianę\n
    eps     - jeżeli podany funkcja zwróci True, gdy\n
              będzie trzeba zatrzymać szukanie
    '''
    # utwórz wektor różnicowy
    diff = []
    for i in range(len(prev_xs)):
        diff.append(xs[i]-prev_xs[i])
    # weź maksymalną absolutną zmianę
    max_diff = max(list(map(abs, diff)))
    # jeżeli eps to None, zwróć zmianę
    if (eps == None): return max_diff
    # zwróć czy zmiana jest mniejsza
    # od zakładanej (eps powinien być < 1)
    return max_diff < eps*max(list(map(abs, xs)))


# załaduj macierz
matrix = []
with open(input("Podaj nazwę pliku z macierzą: ")) as file_in:
    for line in file_in:
        line = line.replace('\n', '')
        matrix.append(list(map(float, line.split())))

# wydziel z macierzy spodziewane wyniki
equals = []
for line in matrix:
    equals.append(line.pop())

# przerób wszystkie macierze/wektory na numpy'owe
matrix = np.array(matrix)
equals = np.array(equals)
xs = np.zeros(len(equals))

# sprawdź macierz
if (not lib.is_matrix_square(matrix)):
    print("Macierz nie jest kwadratowa !!!")
    exit()
if (not lib.is_matrix_convergent(matrix)):
    print("Macierz nie jest zbieżna!!!")
    exit()

''' trzeba napisać funkcję której warunkiem stopu będzie coś
tam związane z wektorem błędu (coś jest na wiki) '''
#

''' przykład jak zrobić funkcję szukającą po błędzie A '''
# xs = search(matrix, equals, xs)
# prev_xs = xs.copy()
# xs = search(matrix, equals, xs)
# i = 2
# while not error_A(prev_xs, xs, 0.000001):
#     i += 1
#     prev_xs = xs.copy()
#     xs = search(matrix, equals, xs)



''' przykład jak zrobić funkcję szukającą iteracyjnie '''
# for i in range(100):
#     prev_xs = xs
#     xs = search(matrix, equals, xs)
    

