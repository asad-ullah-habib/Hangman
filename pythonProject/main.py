import math


def build_pyramid(b , c):
    levels = math.ceil(b / 2)
    for i in range(levels + 1):
        space = math.floor(b / 2)
        print(' ' * space + c + ' ' * space)


b = 9
c = '*'
build_pyramid(b, c)
