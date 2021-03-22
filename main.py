import numpy as np
import matrix_lib as lib

matrix = []
with open("matrix.txt") as file_in:
    for line in file_in:
        line = line.replace('\n', '')
        matrix.append(list(map(int, line.split())))
matrix = np.array(matrix)

if (not lib.is_matrix_square(matrix)):
    print("Macierz nie jest kwadratowa !!!")
    exit()
if (not lib.is_matrix_convergent(matrix)):
    print("Macierz nie jest zbieżna!!!")
    exit()
    
print(matrix)