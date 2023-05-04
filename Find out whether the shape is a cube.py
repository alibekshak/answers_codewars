def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    else:
        return volume == side * side * side 