def descending_order(num):
    a = sorted([i for i in str(num)], reverse=True)
    return int(''.join(a))