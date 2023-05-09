# from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
# by Thuwarakesh Murallie  Mar 13, 2023	

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper


@timing_decorator
def my_function():
    # some code here
    time.sleep(1)  # simulate some time-consuming operation
    return
