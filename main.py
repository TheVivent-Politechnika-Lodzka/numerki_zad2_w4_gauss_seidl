import numpy as np
import matrix_lib as lib

# napisać szukańsko wg tego
# https://pl.wikipedia.org/wiki/Metoda_Gaussa-Seidla#Uk%C5%82ad_trzech_r%C3%B3wna%C5%84_liniowych
# search(), to wykonanie jednej iteracji
def search(M, X):
    for i in range(len(M)):
        sum = 0
        


    return X




# załaduj macierz
matrix = []
with open("matrix.txt") as file_in:
    for line in file_in:
        line = line.replace('\n', '')
        matrix.append(list(map(int, line.split())))

# wydziel z macierzy spodziewane wyniki
expected_results = []
for line in matrix:
    expected_results.append(line.pop())

matrix = np.array(matrix)
expected_results = np.array(expected_results)
current_results = np.zeros(len(expected_results))

# sprawdź macierz
if (not lib.is_matrix_square(matrix)):
    print("Macierz nie jest kwadratowa !!!")
    exit()
if (not lib.is_matrix_convergent(matrix)):
    print("Macierz nie jest zbieżna!!!")
    exit()

print(matrix)
print(expected_results)
print(current_results)