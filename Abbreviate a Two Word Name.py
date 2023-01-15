def abbrev_name(name):
    w = name.split(" ")
    l = [i[0].upper() for i in w]
    return ".".join(l)