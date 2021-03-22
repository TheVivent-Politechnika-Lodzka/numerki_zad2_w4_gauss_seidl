import numpy as np
from numpy.core.defchararray import equal
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




# załaduj macierz
matrix = []
with open("matrix.txt") as file_in:
    for line in file_in:
        line = line.replace('\n', '')
        matrix.append(list(map(float, line.split())))

# wydziel z macierzy spodziewane wyniki
equals = []
for line in matrix:
    equals.append(line.pop())

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

for i in range(2):
    xs = search(matrix, equals, xs)
    print(xs)
