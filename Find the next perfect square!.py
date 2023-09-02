import math
def find_next_square(sq):
    sqr = sq ** 0.5
    return (sqr + 1) ** 2 if sqr.is_integer() == True else -1