def reverse(st):
    # Your Code Here
    baza = ' '
    s = st.split()
    t = list(reversed(s))
    r = baza.join(t)
    return r