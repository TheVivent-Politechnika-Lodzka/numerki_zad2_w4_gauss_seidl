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
def change_of_components(prev_xs, xs, eps=None):
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
def change_of_diff_vec(M, out, X, eps=None):
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