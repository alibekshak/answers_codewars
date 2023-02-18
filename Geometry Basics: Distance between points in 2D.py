import math
def distance_between_points(a, b):  
    a = [a.x, a.y]
    b = [b.x, b.y]
    
    return math.dist(a, b)