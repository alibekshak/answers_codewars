def remove_smallest(numbers):
    working_numbers = numbers.copy()
    if numbers == []:
        return []
    for i in numbers:
        if i == min(numbers):
            working_numbers.remove(i)
            return working_numbers