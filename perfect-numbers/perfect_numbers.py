def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum_of_divisors = sum([divisor if number % divisor == 0 else 0\
                      for divisor in range(number-1, 0, -1)])
    if sum_of_divisors == number:
        return "perfect"
    elif sum_of_divisors > number:
        return "abundant"
    elif sum_of_divisors < number:
        return "deficient"