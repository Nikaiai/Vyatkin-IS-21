from random import randint
a = randint(5, 20)
b = randint(5, 20)
c = randint(5, 20)


def triangle_perimeter(z=a, x=b, v=c):
    return round(z+x+v, 2)


def triangle_area(z=a, x=b, v=c):
    p = triangle_perimeter(z, x, v)/2
    return round(p*(p-z)*(p-x)*(p-c)**0.5, 2)
