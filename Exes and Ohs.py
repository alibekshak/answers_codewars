def xo(s):
    o = s.lower().count("o")
    x = s.lower().count("x")
    
    if o == x:
        return True
    elif o != x:
        return False 
    else: 
        return True