def warn_the_sheep(queue):
    number = len(queue) - queue.index("wolf") - 1

    if queue[-1] == 'wolf':
        return "Pls go away and stop eating my sheep"

    else:
        return f"Oi! Sheep number {number}! You are about to be eaten by a wolf!"