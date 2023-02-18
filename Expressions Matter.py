def expression_matter(a, b, c):
    baza = [
        a * (b + c),
        a * b * c,
        a + b * c,
        (a + b) * c,
        a + b + c
    ]
    return max(baza)