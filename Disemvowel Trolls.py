def disemvowel(string_):
    vowels = "AEIOUaeiou"
    baza = ""
    for i in string_:
        if i not in vowels:
            baza += i
            
    return baza 