def maskify(cc):
    if len(cc) <= 3:
        return cc
    return ''.join("#" * (len(cc) - 4) + cc[-4:])