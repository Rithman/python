from functools import wraps


def logger(func):
    @wraps(func)
    def wraper(arg):
        result = func(arg)
        return f'{func.__name__}({arg}: {type(arg)}) result = {result} ({type(result)})'

    return wraper


@logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
