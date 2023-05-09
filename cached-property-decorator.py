# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@cached_property: Cache the Result of a Method as an Attribute
Python 3.8 introduced a new powerful decorator to the functool module — @cached_property. It can transform a method of a class into a property whose value is computed once and then cached as a normal attribute for the life of the instance.

Here’s an example:

from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(10)
print(circle.area)
# prints 314.0
print(circle.area)
# returns the cached result (314.0) directly
In the above code, we decorated the area method through the @cached_property. So there are no repetitive calculations for circle.area of the same unchanged instance.