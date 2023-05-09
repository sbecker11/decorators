# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@classmethod: Define Class Methods in a Python Class
Inside a Python class, there are 3 possible types of methods:

Instance methods: methods that are bound to an instance. They can access and modify the instance data. An instance method is called on an instance of the class, and it can access the instance data through the self parameter.
Class methods: methods that are bound to the class. They can’t modify the instance data. A class method is called on the class itself, and it receives the class as the first parameter, which is conventionally named cls.
Static methods: methods that are not bound to the instance or the class.
The instance methods can be defined as normal Python functions as long as its first parameter is self. However, to define a class method, we need to use the @classmethod decorator.

To demonstrate, the following example defines a class method which can be used to get a Circle instance through a diameter:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


c = Circle.from_diameter(8)
print(c.radius)  # 4.0
print(c.diameter)  # 8.0
