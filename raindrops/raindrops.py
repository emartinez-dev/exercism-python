import enum


def convert(number):
    sounds = (number % 3 == 0, number % 5 == 0, number % 7 == 0)
    temp_string = ""
    for n, sound in enumerate(sounds):
        if sound == True:
            if n == 0:
                temp_string += "Pling"
            if n == 1:
                temp_string += "Plang"
            if n == 2:
                temp_string += "Plong"
    return temp_string if temp_string != "" else str(number)
