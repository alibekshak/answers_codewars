def get_count(sentence):
    num = 0
    for vow in ["a", "e", "i", "o", "u"]:
        num += sentence.count(vow)
    return num
            