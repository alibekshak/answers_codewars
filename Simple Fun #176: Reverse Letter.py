def reverse_letter(string):
    nam = "1234567890"
    a = "!@£$%^&*()?[]{}:;''-+#€¡¢∞^&*_+?><≥÷≤…æ««‘“/=\\//,.~|` "
    b = string.translate({ord (i): None for i in nam})
    c = b.translate({ord (i): None for i in a})
    d = c.translate({ord (i): None for i in '"'})
    return d[::-1]