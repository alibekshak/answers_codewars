def string_clean(s):
    return "".join("" if i.isdigit() else i for i in s)