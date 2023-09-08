def dont_give_me_five(start,end):
    number = 0
    for i in range(start, end+1):
        if "5" in str(i):
            continue
        number += 1
    return number 