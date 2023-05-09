# from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
# by 
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

