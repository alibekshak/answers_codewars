def distinct(seq):
    baza = []
    for i in seq:
        if i not in baza:
            baza.append(i)
    return baza