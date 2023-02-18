def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    for i in range(1, human_years+1):
        if i == 1:
            cat += 15
            dog += 15
        elif i == 2:
            cat += 9
            dog += 9
        else: 
            dog += 5
            cat += 4
    return [human_years, cat, dog]