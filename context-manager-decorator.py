# from https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

@contextmanager: Make a Customized Context Manager
Python has a context manager mechanism to help you manage resources properly.

Mostly, we just need to use the with statements:

with open("test.txt",'w') as f:
    f.write("Yang is writing!")
As the above code shows, we can open a file using the with statement so it will be closed automatically after being written. We don’t need to call the f.close() function explicitly to close the file.

Sometimes, we need to define a customized context manager for some special requirements. In this case, the @contextmanager decorator is our friend.

For instance, the following code implements a simple customized context manager which can print corresponding information when a file is opening or closing.

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print("The file is opening...")
    file = open(filename,mode)
    yield file
    print("The file is closing...")
    file.close()

with file_manager('test.txt', 'w') as f:
    f.write('Yang is writing!')
# The file is opening...
# The file is closing...