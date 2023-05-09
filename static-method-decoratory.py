# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@staticmethod: Define Static Methods in a Python Class
As mentioned, static methods are not bound to an instance or a class. They are included in a class simply because they logically belong there.

Static methods are commonly used in utility classes that perform a group of related tasks, such as mathematical calculations. By organizing related functions into static methods within a class, our code will become more organized and easier to understand.

To define a static method, we just need to use the @staticmethod decorator. Let’s see an example:

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = None

    def set_nickname(self, name):
        self.nickname = name

    @staticmethod
    def suitable_age(age):
        return 6 <= age <= 70


print(Student.suitable_age(99)) # False
print(Student.suitable_age(27)) # True
print(Student('yang', 'zhou').suitable_age(27)) # True