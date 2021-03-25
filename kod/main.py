import numpy as np
import matrix_lib as lib
import gauss_seidl as gs
import charts

def search_by_iterations(i, matrix, equals, xs):
    points = [] # tablica na punkty [iteracja, zmiana wektora, zmiana składowych] do wykresu
    X = xs.copy() # zabezpieczenie przed nadpisywaniem xs
    prev_x = []   # tablica na poprzedni wynik
    for i in range(i):
        prev_x = X.copy()
        X = gs.search(matrix, equals, X)
        points.append([i, gs.change_of_diff_vec(matrix, equals, X), gs.change_of_components(prev_x, X)])
    # zwraca:
    # liczbę iteracji
    # zmianę składowych
    # zmianę wektora zmian
    # punkty na wykres
    # wynik
    return \
        i,\
        gs.change_of_components(prev_x, X),\
        gs.change_of_diff_vec(matrix, equals, X),\
        points,\
        X


def search_by_diff_vec(eps, matrix, equals, xs):
    points = [] # tablica na punkty [iteracja, zmiana wektora, zmiana składowych] do wykresu
    X = xs.copy()   # zabezpieczenie przed nadpisywaniem xs
    prev_x = []     # tablica na poprzedni wynik
    i = 0
    while not gs.change_of_diff_vec(matrix, equals, X, eps):
        i += 1
        prev_x = X.copy()
        X = gs.search(matrix, equals, X)
        points.append([i, gs.change_of_diff_vec(matrix, equals, X), gs.change_of_components(prev_x, X)])

    # zwraca:
    # liczbę iteracji
    # zmianę składowych
    # zmianę wektora zmian
    # punkty na wykres
    # wynik
    return \
        i,\
        gs.change_of_components(prev_x, X),\
        gs.change_of_diff_vec(matrix, equals, X),\
        points,\
        X

def search_by_components(eps, matrix, equals, xs):
    points = [] # tablica na punkty [iteracja, zmiana wektora, zmiana składowych] do wykresu
    X = xs.copy()   # zabezpieczenie przed nadpisywaniem xs
    prev_x = []     # tablica na poprzedni wynik
    i = 0
    while True:
        i += 1
        prev_x = X.copy()
        X = gs.search(matrix, equals, X)
        points.append([i, gs.change_of_diff_vec(matrix, equals, X), gs.change_of_components(prev_x, X)])
        if gs.change_of_components(prev_x, X, eps): break
    # zwraca:
    # liczbę iteracji
    # zmianę składowych
    # zmianę wektora zmian
    # punkty na wykres
    # wynik
    return \
        i,\
        gs.change_of_components(prev_x, X),\
        gs.change_of_diff_vec(matrix, equals, X),\
        points,\
        X



# załaduj macierz
matrix = []
with open("macierze/" + input("Podaj nazwę pliku z macierzą: ")) as file_in:
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

print()
print("1. Iteracyjnie")
print("2. Przez śledzenie zmian składowych")
print("3. Przez śledzenie wektora różnic")
opt = int(input("Wybierz warunek stopu: "))


i, eps, err_comp, err_diff_vec = 0, 0, 0, 0
points = []
result = []
if (opt == 1):
    i = int(input("liczba iteracji do wykonania: "))
    i, err_comp, err_diff_vec, points, result = search_by_iterations(i, matrix, equals, xs)
if (opt == 2 or opt == 3):
    eps = float(input("podaj epsilon: "))
    if (opt == 2):
        i, err_comp, err_diff_vec, points, result = search_by_components(eps, matrix, equals, xs)
    if (opt == 3):
        i, err_comp, err_diff_vec, points, result = search_by_diff_vec(eps, matrix, equals, xs)
print()
print("##################################")
print("Wybrana metoda szukania: ", end="")
if opt == 1: print("iteracyjnie")
if opt == 2: print("śledzenie zmian składowych")
if opt == 3: print("śledzenie wektora różnic")

print("ilość iteracji:          " + str(i))
if opt == 2 or opt == 3:
    print("epsilon:                 " + str(eps))
print("błąd zmian składowych:   " + str(err_comp))
print("błąd wektora różnic:     " + str(err_diff_vec))
print("Wynik:                   ", end="")
print(result)
print("##################################")

# UWAGA!!! działa tylko dla itercyjnego, bo reszta nie jest napisana
charts.create_chart(np.array(points).transpose(), input("nazwij plik wykresu: "))