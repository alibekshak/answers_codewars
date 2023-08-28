def find_short(s):
    # your code here
    split_s = s.split(" ")
    split_s.sort(key=len)
    return len(split_s[0])