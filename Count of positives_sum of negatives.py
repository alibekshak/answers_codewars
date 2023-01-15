def count_positives_sum_negatives(arr):
    c = 0
    t = 0
    for i in arr:
        if i > 0:
            c += 1
        elif i < 0:
            t += i
    return [c, t] if len(arr) != 0 else []