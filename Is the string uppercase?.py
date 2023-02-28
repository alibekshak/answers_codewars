import re
def is_uppercase(inp):
    if inp.upper() == inp:
        return True
    elif re.match('[a-z]',inp) != None:
        return False
    return False