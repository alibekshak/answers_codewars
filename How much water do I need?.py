def how_much_water(water, load, clothes):
    if clothes > load * 2 :
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
         return float(f"{water * 1.1 ** (clothes - load):0.2f}")