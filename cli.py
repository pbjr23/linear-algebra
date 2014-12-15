import code
from app.lib import *

vars = globals()
vars.update(locals())
shell = code.InteractiveConsole(vars)
print """Welcome to the Python Linear Algebra toolkit command line interface.
Feel free to explore around in the Matrix class.
To get started, try making a Matrix like this:
    >>> my_matrix = Matrix(2, 3, 2) \
"""
shell.interact("")
