def divisors(integer):
    return [i for i in range(2, integer) if not integer % i ] or f"{integer} is prime"