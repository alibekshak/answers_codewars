def is_palindrome(s):
    return True if s[::-1].lower() == s.lower() else False 