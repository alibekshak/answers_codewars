def array(string):
    baza = string.split(",")[1:-1]
    if len(baza) == 0:
        return None
    return ' '.join(baza)