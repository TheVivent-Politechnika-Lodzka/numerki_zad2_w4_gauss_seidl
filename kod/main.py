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
    eps     - jeżeli nie podany, funkcja zwróci zmianę\n
    eps     - jeżeli podany, funkcja zwróci True, gdy\n
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

# sprawdza czy maksymalne odchylenie jest mniejsze od założonego
# na podstawie wektora zmian (vec)
def error_B(M, out, X, eps=None):
    '''
    M   - macierz wejściowa\n
    out - wektor wyników\n
    X   - wektor obliczonych x'ów\n
    eps - jeżeli nie podany, funkcja zwróci zmianę\n
    eps - jeżeli podany, funkcja zwróci True, gdy\n
          trzeba zatrzymać szukanie
    '''
    vec = []
    for i in range(len(M)):
        line = M[i]
        sum = 0
        # oblicz każde równanie w macierzy
        # używając osiągniętych x'ów
        for j in range(len(line)):
            sum += (line[j]*X[j])
        # wrzuć do wektora różnic, różnicę
        # między obliczonym wynikiem, a oczekiwanym
        vec.append(out[i] - sum)
    # znajdź maksymalne odchylenie
    max_diff = max(list(map(abs, vec)))
    # jeżeli eps nie podany, zwróć różnicę
    if (eps == None): return max_diff
    # jeżeli eps podany, zwróć czy zatrzymać szukanie
    return max_diff < eps

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

''' przykład jak zrobić funkcę szukającą po błędzie B '''
# i = 0
# while not error_B(matrix, equals, xs, 0.00001):
#     i += 1
#     xs = search(matrix, equals, xs)


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
    

