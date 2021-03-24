import matplotlib.pyplot as plt

def create_chart(points, filename):
    '''
    points   - punkty po transpozycji\n
    filename - nazwa pliku jak będzie zapisany
    '''
    # narysuj linie na 0,0
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # przekształć i narysuj punkty
    plt.plot(points[0], points[1], "bo")

    # pokaż
    # plt.show()

    # zapisz
    plt.savefig(filename + ".png")