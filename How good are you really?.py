def better_than_average(class_points, your_points):
    sum_class = sum(class_points)/len(class_points)
    if sum_class <= your_points:
        return True
    return False 