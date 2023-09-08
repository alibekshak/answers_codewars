def series_sum(n):
    n_result = []
    for i in range(1, 3*n - 1, 3):
        n_result.append(1/i)
    return "{:.2f}".format(sum(n_result))