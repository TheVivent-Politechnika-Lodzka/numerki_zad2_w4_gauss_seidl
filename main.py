import numpy as np


matrix = []
with open("matrix.txt") as file_in:
    for line in file_in:
        line = line.replace('\n', '')
        matrix.append(list(map(int, line.split())))
matrix = np.array(matrix)

print(matrix)