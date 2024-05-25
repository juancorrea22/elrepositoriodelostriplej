def binary_to_ascii(binary):
    ascii_char = chr(int(binary, 2))
    ascii_code = format(int(binary, 2), 'x')
    return f"{ascii_char}-{ascii_code}"