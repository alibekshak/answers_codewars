def hello(name=""):
    return f"Hello, {name.capitalize()}!" if name or len(name) > 1 else "Hello, World!"