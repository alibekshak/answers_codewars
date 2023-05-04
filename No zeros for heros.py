def no_boring_zeros(n):
    if n == 0:
        return n
    else:
        n = str(n)
        for i in n:
            if n[-1] == "0":
                n = n.rstrip('0')
        return int(n)