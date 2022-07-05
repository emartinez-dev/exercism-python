def square_of_sum(number):
    numbers = range(1, number + 1)
    return sum(numbers)**2


def sum_of_squares(number):
    numbers = range(1, number + 1)
    squares = map(lambda x: x * x, numbers)
    return sum(squares)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)