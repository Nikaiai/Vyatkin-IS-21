from random import randint
default_radius = randint(5, 20)


def circle_perimeter(s=default_radius):
    return round(2 * 3.14 * s, 2)


def circle_area(s=default_radius):
    return round(s**2 * 3.14, 2)
