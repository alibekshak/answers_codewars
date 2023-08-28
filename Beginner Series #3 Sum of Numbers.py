def get_sum(a,b):
    if a == b:
        return a
    elif b < a:
        return sum(list(range(b, a+1)))
    else:
        return sum(list(range(a, b+1)))