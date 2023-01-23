def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return f"{name} plays banjo"
    else:
         return f"{name} does not play banjo"