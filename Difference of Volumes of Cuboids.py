def find_difference(a, b):
    a_all = a[0] * a[1] * a[2]
    b_all = b[0] * b[1] * b[2]
    difer = a_all - b_all
    if difer < 0:
        return difer * -1
    return difer