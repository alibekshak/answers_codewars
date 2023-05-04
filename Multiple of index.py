def multiple_of_index(arr):
    baza = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            baza.append(arr[i])
    return baza
            