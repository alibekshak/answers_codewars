def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    elif len(pin) == 6 and pin.isdigit():
        return True
    return False