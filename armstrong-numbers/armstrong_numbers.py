def is_armstrong_number(number):
    number = str(number)
    number_of_digits = len(number)
    temp_number = 0
    for n in range(number_of_digits):
        temp_number += int(number[n]) ** number_of_digits
    return temp_number == int(number)