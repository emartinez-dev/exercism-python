import string

def is_isogram(_string):
    letter_frequency = {}
    alphabet = list(string.ascii_lowercase)
    for letter in _string.lower():
        if letter in alphabet:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    return list(letter_frequency.values()) == [1] * len(letter_frequency.values())