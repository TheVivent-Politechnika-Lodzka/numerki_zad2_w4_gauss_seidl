import numpy as np
import matrix_lib as lib
import gauss_seidl as gs
import charts

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

print()
print("1. Iteracyjnie")
print("2. Przez śledzenie zmian składowych")
print("3. Przez śledzenie wektora różnic")
opt = int(input("Wybierz warunek stopu: "))


i, eps, err_com, err_diff_vec = 0, 0, 0, 0
points = []
result = []
if (opt == 1):
    i = int(input("liczba iteracji do wykonania: "))
    # i, err_comp, err_diff_vec, points, result = # funkcja która to wszystko zwróci
if (opt == 2 or opt == 3):
    eps = float(input("podaj epsilon: "))
    # if (opt == 2):
        # i, err_comp, err_diff_vec, points, result = # funkcja która to wszystko zwróci
    # if (opt == 3):
        # i, err_comp, err_diff_vec, points, result = # funkcja która to wszystko zwróci
print()
print("##################################")
print("Wybrana metoda szukania: ", end="")
if opt == 1: print("iteracyjnie")
if opt == 2: print("śledzenie zmian składowych")
if opt == 3: print("śledzenie wektora różnic")

print("ilość iteracji:          " + str(i))
if opt == 2 or opt == 3:
    print("epsilon:                 " + str(eps))
print("błąd zmian składowych:   " + str(err_com))
print("błąd wektora różnic:     " + str(err_diff_vec))
print("Wynik:                   ", end="")
print(result)
print("##################################")

# gotowa funkcja do wyrysowania wykresu. Jest zakomentowana, bo nie ma
# jeszcze funkcji które zwracają `points`
# charts.create_chart(np.array(points).transpose(), input("nazwij plik wykresu: "))


'''
przykład jak zrobić funkcję której warunkiem stopu
będzie śledzenie wektora różnic
'''
# i = 0
# while not error_B(matrix, equals, xs, 0.00001):
#     i += 1
#     xs = search(matrix, equals, xs)


'''
przykład jak zrobić funkcję której warunkiem stopu
będzie śledzenie zmian składowych
'''
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
    

