# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@lru_cache: Speed Up Your Programs by Caching
The simplest way to speed up your Python functions with caching tricks is to use the @lru_cache decorator.

This decorator can be used to cache the results of a function, so that subsequent calls to the function with the same arguments will not be executed again.

It is especially helpful for functions that are computationally expensive or that are called frequently with the same arguments.

Let’s see an intuitive example:

import time


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.18129450 seconds
The above program calculates the Nth Fibonacci number with a Python function. It’s time-consuming cause when you calculate the fibonacci(30), many previous Fibonacci numbers will be calculated many times during the recursion process.

Now, let’s speed it up with the @lru_cache decorator:

from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.00002990 seconds
As the above code shows, after using the @lru_cache decorator, we can get the same result in 0.00002990 seconds, which is super faster than the previous 0.18129450 seconds.

The @lru_cache decorator has a maxsize parameter that specifies the maximum number of results to store in the cache. When the cache is full and a new result needs to be stored, the least recently used result is evicted from the cache to make room for the new one. This is called the least recently used (LRU) strategy.

By default, the maxsize is set to 128. If it is set to None, as our example, the LRU features are disabled and the cache can grow without bound.

