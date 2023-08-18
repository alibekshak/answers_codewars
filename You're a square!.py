import math
def is_square(n):    
    if n < 0: 
        return False
    ans = math.sqrt(n)
    if ans ** 2 == n: 
        return True
    else: 
        return False 