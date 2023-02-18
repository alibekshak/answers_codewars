import math
def square_or_square_root(arr):
    baza = []
    for i in arr:
        if math.sqrt(i) == int(math.sqrt(i)):
            baza.append(int(math.sqrt(i)))
        else:
            baza.append(i ** 2)
    return baza