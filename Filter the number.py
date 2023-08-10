def filter_string(string):

    baza = ""
    if string.isdigit():
        return int(string)
    else:
        for i in string:
            
            if i.isdigit():
                baza += i
        return int(baza)
            