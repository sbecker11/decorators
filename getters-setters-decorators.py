# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@property: Setting Up Getters and Setters for Python Classes
Getters and setters are important concepts in object-oriented programming(OOP).

For each instance variable of a class, a getter method returns its value while a setter method sets or updates its value. Given this, getters and setters are also known as accessors and mutators, respectively.

They are used to protect your data from being accessed or modified directly and unexpectedly.

Different OOP languages have different mechanisms to define getters and setters. In Python, we can simply use the @property decorator.

class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError('The score must be between 0 ~ 100!')

Yang = Student()

Yang.score=99
print(Yang.score)
# 99

Yang.score = 999
# ValueError: The score must be between 0 ~ 100!
As the above example shows, the score variable cannot be set as 999, which is a meaningless number. Because we restricted its acceptable range inside the setter function using the @property decorator.

Without doubt, adding this setter can successfully avoid unexpected bugs or results.

