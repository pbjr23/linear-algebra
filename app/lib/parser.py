from matrix import Matrix
from functools import wraps
import random


@latex
def produce_output(s):
    return eval(parse_string(s))


def randomize(rows, columns, start=-10, end=10):
    """Creates a random matrix with the specified number of rows and columns.
    If no range is specified, it is assumed to be from -10 to 10. """
    return Matrix([[random.randint(start, end) for _ in range(columns)]
                   for _ in range(rows)])


def transpose(m):
    """Takes in a matrix returns the transpose."""
    return m.transpose()


def parse_string(s):
    """Formats the raw input string correctly so it can be evaluated
    on the backend properly, eg: by adding Matrix() around matrices."""
    brackets = 0
    offset = 0
    s = s.replace('^', '**').lower()
    s = s.replace('random', 'randomize')
    list_s = list(s)
    output = list(s)
    for i, char in enumerate(list_s):
        if char == '[' and brackets == 0:
            output.insert(i+offset, "Matrix(")
            offset += 1
            brackets += 1
        elif char == ']' and brackets == 1:
            output.insert(offset + i + 1, ')')
            brackets -= 1
            offset += 1
        elif char == '[':
            brackets += 1
        elif char == ']':
            brackets -= 1
    return ''.join(output)


def latexify(matrix_object):
    """Converts a matrix to a LaTeX representation suitable for printing"""
    start = '$\\begin{bmatrix}'
    end = '\end{bmatrix}$'
    m = matrix_object.matrix
    m = [[str(col) for col in row] for row in m]
    m = '\\\\'.join([' & '.join(row) for row in m])
    return start + m + end


def latex(f):
    """Custom decorator to output result in LaTeX using latexify"""
    @wraps(f)
    def decorated(*args, **kwargs):
        return latexify(f(*args, **kwargs))
    return decorated
