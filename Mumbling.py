def accum(s):
    index = 1
    result = []
    for i in s:
        i *= index
        i = i.capitalize()
        index += 1
        result.append(i)
    return "-".join(result)