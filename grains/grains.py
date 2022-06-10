def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    total_rice = 0
    for square_n in range(1, 65):
        total_rice += square(square_n)
    return total_rice