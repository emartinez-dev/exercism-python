import string

def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)
    used_letters = []

    for letter in sentence.lower():
        if letter in alphabet and letter not in used_letters:
            used_letters.append(letter)
    return sorted(used_letters) == alphabet