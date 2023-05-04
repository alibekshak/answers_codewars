def array_madness(a,b):
    baza1 = 0
    baza2 = 0 
    for i in a:
        baza1 = baza1 + i ** 2
    for j in b:
        baza2 = baza2 + j ** 3
    if baza1 > baza2:
        return True
    return False 