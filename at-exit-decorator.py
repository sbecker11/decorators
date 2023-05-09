# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@atexit.register: Register a Function To Be Executed Upon Normal Program Termination
The @register decorator from the atexit module can allow us to execute a function when the Python interpreter is exiting.

This decorator is very useful for performing final tasks, such as releasing resources or just saying goodbye! 👋

Here is an example:

import atexit

@atexit.register
def goodbye():
    print("Bye bye!")

print("Hello Yang!")
The outputs are:

Hello Yang!
Bye bye!
As the example shows, due to the use of the @register decorator, the terminal printed “Bye bye!” even if we didn’t call the goodbye function explicitly.