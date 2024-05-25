def word_to_binary(word):
    return ' '.join(format(ord(char), '08b') for char in word)
