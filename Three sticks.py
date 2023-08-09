def maxlen(L1,L2):
    ma = max(L1, L2)
    mi = min(L1, L2)
    if ma - mi - mi - mi > 0: return ma/3
    if ma - mi - mi > 0: return mi 
    return ma/2