def points(games):
    p = 0
    for i in games:
        g = i.split(":")
        if g[0] > g[1]:
            p += 3
        elif g[0] == g[1]:
            p += 1
    return p