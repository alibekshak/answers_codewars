def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary * 10}"
    else:
        return f"${salary}"