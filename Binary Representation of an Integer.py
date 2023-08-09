def show_bits(n):
    if n >= 0:
        return [int(i) for i in format(n, "b").zfill(32)]
    else:
    
        n = 2**32 + n
        return [int(i) for i in format(n, "b").zfill(32)]