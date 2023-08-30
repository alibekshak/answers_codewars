def longest(a1, a2):
    set_a1_a2 = set(a1 + a2)
    return "".join(sorted(set_a1_a2)) 