def to_jaden_case(string):
    split_string = string.split(" ")
    return " ".join(i.capitalize() for i in split_string)