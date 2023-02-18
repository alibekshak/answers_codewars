def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [i for i in birds if i not in geese]