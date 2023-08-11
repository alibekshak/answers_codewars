def high_and_low(numbers):
    a = numbers.split(" ")
    b = sorted(a, key=int)
    return b[-1] + " " + b[0]