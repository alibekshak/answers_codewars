def number(lines):
    count = 1
    number_letter = []
    for i in lines:
        number_letter.append(f"{count}: {i}")
        count += 1
    return number_letter