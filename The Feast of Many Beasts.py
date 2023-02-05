def feast(beast, dish):
    if beast[0] != dish[0]:
        return False
    return beast[-1] == dish[-1]