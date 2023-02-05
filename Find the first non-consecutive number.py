def first_non_consecutive(arr):
    f = 1
    for i in arr:
        if f < len(arr) and arr[f] - arr[f-1] != 1:
            return arr[f]
        f += 1
    return None