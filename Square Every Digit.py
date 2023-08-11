def square_digits(num):

    y = [int(j) ** 2 for j in str(num)]
    x = int("".join(map(str, y)))
    return x