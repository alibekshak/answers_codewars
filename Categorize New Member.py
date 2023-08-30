def open_or_senior(data):
    return ["Senior" if year >= 55 and handicap > 7 else "Open" for year, handicap in data]
