def number(bus_stops):
    people_in = 0
    people_out = 0
    for j in range(0,len(bus_stops)):
        people_in += bus_stops[j][0]
        people_out += bus_stops[j][1]
    return people_in - people_out