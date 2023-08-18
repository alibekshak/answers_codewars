def is_isogram(string):
    chek_string = []
    word_lower = string.lower()
    
    for i in word_lower:
        if i.isalpha():
            if i in chek_string:
                return False
            chek_string.append(i)
    return True
        