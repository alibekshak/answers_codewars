def str_count(strng, letter):
    num = 0
    for i in strng:
        if i == letter:
            num += 1
    return num