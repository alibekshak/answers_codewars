def get_grade(s1, s2, s3):
    s = (s1+s2+s3) // 3
    if 90 <= s <= 100:
        return "A"
    elif 80 <= s <= 90:
        return "B"
    elif 70 <= s <= 80:
        return "C"
    elif 60 <= s <= 70:
        return "D"
    else:
        return "F"