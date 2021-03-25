import matplotlib.pyplot as plt

def create_chart(points, filename):
    '''
    points   - punkty po transpozycji\n
    filename - nazwa pliku jak będzie zapisany
    '''
    # narysuj linie na 0,0
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # narysuj punkty
    plt.plot(points[0], points[1], "bo", label="różnica wektora różnic")
    plt.plot(points[0], points[2], "r.", label="różnica składowych")
    plt.legend(loc="upper right")

    # pokaż
    # plt.show()

    # zapisz
    plt.savefig("wykresy/" + filename + ".png")