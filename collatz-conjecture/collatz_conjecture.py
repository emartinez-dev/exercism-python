def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    n_steps = 0
    while number != 1:
        number = 3 * number + 1 if number % 2 != 0 else number / 2
        n_steps += 1
    return n_steps