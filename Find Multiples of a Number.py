def find_multiples(integer, limit):
    baza = []
    for i in range(1, limit+1):
        if i % integer == 0:
            baza.append(i)
    return baza