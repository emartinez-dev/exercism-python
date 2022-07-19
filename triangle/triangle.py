def valid_triangle(sides: list):
    try:
        assert len(sides) == 3
        a,b,c = sides
        assert a > 0
        assert b > 0
        assert c > 0
        assert a + b >= c
        assert b + c >= a
        assert a + c >= b
        return True
    except:
        return False


def equilateral(sides):
    if valid_triangle(sides):
        a,b,c = sides
        return a == b and b == c
    return False


def isosceles(sides):
    if valid_triangle(sides):
        a,b,c = sides
        return a == b or b == c or a == c
    return False


def scalene(sides):
    if valid_triangle(sides):
        a,b,c = sides
        return a != b and b != c and a != c
    return False