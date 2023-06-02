def flip(d, a):
    if d == 'R':
        return sorted(a) 
    return sorted(a, reverse=True)