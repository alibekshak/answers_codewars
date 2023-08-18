def filter_list(l):
    filter_list = []
    for i in l:
        if type(i) == int:
            filter_list.append(i)
    return filter_list