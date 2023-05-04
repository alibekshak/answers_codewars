import string
def position(alphabet):
    conv = string.ascii_lowercase
    return f"Position of alphabet: {conv.find(alphabet) + 1}"