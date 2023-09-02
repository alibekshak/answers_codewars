import string 
def printer_error(s):
    errors = ""
    control = string.ascii_lowercase[0:13]
    
    for letter in s:
        if letter not in control:
            errors += letter
    return f"{len(errors)}/{len(s)}"