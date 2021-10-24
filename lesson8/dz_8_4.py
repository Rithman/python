from functools import wraps
from math import sqrt


def validator(func):
    @wraps(func)
    def wraper(arg):
        try:
            result = func(arg)
            print(result)
        except ValueError as e:
            print(f'{e}: wrong value {arg}')

    return wraper


@validator
def calc_cube(x):
    return sqrt(x)


calc_cube(-5)
