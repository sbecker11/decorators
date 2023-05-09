# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@total_ordering: A Class Decorator That Fills In Missing Ordering Methods
The @total_ordering decorator from the functools module is used to generate the missing comparison methods for a Python class based on the ones that are defined.

Here's an example:

from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)

print(student1 < student2)  # False
print(student1 > student2)  # True
print(student1 == student3)  # True
print(student1 <= student3) # True
print(student3 >= student2) # True
As the above code illustrated, there are no definitions for __ge__, __gt__, and __le__ methods in the Student class. However, thanks to the @total_ordering decorator, the results of our comparisons between different instances are all correct.

The benefits of this decorator are obvious:

It can make your code cleaner and save your time. Since you don’t need to write all the comparison methods.
Some old classes may not define enough comparison methods. It’s safer to add the @total_ordering decorator to it for further usage.
