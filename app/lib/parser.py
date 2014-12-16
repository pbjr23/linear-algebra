from matrix import Matrix

def produce_output(s):
    return latexify(eval(parse_string(s)))


def parse_string(s):
    """Formats the raw input string correctly so it can be evaluated
    on the backend properly, eg: by adding Matrix() around matrices."""
    brackets = 0
    offset = 0
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

