def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    multip = 0
    sum_multip = 0
    while multip < m:
        multip += n
        if multip >= m:
            break 
        sum_multip += multip
    return sum_multip