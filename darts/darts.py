def score(x, y):
    point = (x**2 + y**2)
    if point <= 1:
        return 10
    if point <= 25:
        return 5
    if point <= 100:
        return 1
    return 0
