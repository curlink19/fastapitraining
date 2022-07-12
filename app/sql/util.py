def transform_password(password: str, step: int = 19, is_back: bool = False):
    if is_back:
        step = -step
    result = ""
    for c in password:
        result += str(chr((ord(c) - ord('a') + step + 26) % 26 + ord('a')))
    return result
