def draw_stairs(n):
    baza = ""
    for i in range(0, n-1):
        baza +=  " " * i + "I\n"
    baza +=  " " * (n-1) + "I"
    return baza 