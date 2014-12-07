def first_nonzero(row):
    pass


def one_position(pos):
    pass


def matrix_check(matrix):
    pass


def space_length(i):
    pass


def dot_product(m1, m2):
    pass


def expanded_dot_product(m1, m2):
    pass


class Matrix(object):
    """Python matrix representation"""

    def __init__(self, *args):
        """Initializes the matrix
        Accepted entries:
          foo = Matrix(2, 3) <-> Creates a 2x3 matrix with all values as 0
          foo = Matrix(4, 3, 2) <-> Creates a 4x3 matrix with all values as 2
          foo = Matrix([[1,2], [3,4]]) <-> Turns the list into a Matrix object
        """
        if len(args) == 2:
            self.rows = args[0]
            self.columns = args[1]
            self.matrix = [[0] * args[1] for x in range(args[0])]
        if len(args) == 3:
            self.rows = args[0]
            self.columns = args[1]
            self.matrix = [[args[2]] * args[1] for x in range(args[0])]
        if len(args) == 1 and matrix_check(args[0]):
            if not any(isinstance(l, list) for l in args[0]):
                self.rows = 1
                self.columns = len(args[0])
            else:
                self.rows = len(args[0])
                self.columns = len(args[0][0])
            self.matrix = args[0]
        if (len(args) == 1 and not matrix_check(args[0])) or len(args) > 3:
            raise Exception("Invalid format given")

    def __str__(self):
        """Prints out the matrix as a string, without any brackets around it
           Format:  1 2     <-> print Matrix([[1, 2], [3, 4]])
                    3 4
        """
        if not any(isinstance(l, list) for l in self.matrix):
            self.matrix = [self.matrix]
        return '\n'.join(
            [' '.join(
                [str(element).rjust(space_length(self.matrix))
                    for element in row]) for row in self.matrix]) + "\n"

    def __eq__(self, other):
        """ == Checks if two matrices are equal."""
        return self.matrix == other.matrix

    def __ne__(self, other):
        """!= Check if two matrices are not equal."""
        return not self.__eq__(other)

    def valid_check(self):
        """Checks whether a matrix is valid.
           Eg: Checks whether the dimensions of self.matrix actually
               correspond to self.rows and self.columns
        """
        if not any(isinstance(l, list) for l in self.matrix) and \
                all(isinstance(element, (int, long, float))
                    for element in self.matrix):
            self.matrix = [self.matrix]
            return True
        if len(self.matrix) != self.rows:
            return False
        if not all(len(row) == self.columns for row in self.matrix):
            return False
        for row in self.matrix:
            if len(row) != self.columns:
                return False
        for row in self.matrix:
            for element in row:
                if not isinstance(element, (int, long, float)):
                    return False
        return True

    def same_dimensions_check(self, other):
        """First makes sure both matrices are valid. Then makes sure the
           dimensions are the same for both."""
        assert self.valid_check() and other.valid_check()
        return self.rows == other.rows and self.columns == other.columns

    def multiply_check(self, other):
        """Checks whether the middle dimensions are the same to do matrix
           multiplication."""
        return self.columns == other.rows

    def __add__(self, other):
        """Addition for matrices
           Accepted formats:
              foo = Matrix(2, 2)
              bar = Matrix(2, 2, 5)
              baz = Matrix(2, 2, 4)
              foo + bar <-> returns a matrix of the form Matrix(2, 2, 5)
              bar + baz <-> returns a matrix of the form Matrix(2, 2, 9)
              foo + 2 <-> returns a matrix of the form Matrix(2, 2, 2)
        """
        if isinstance(other, (int, long, float)):
            assert self.valid_check()
            add = Matrix(self.rows, self.columns)
            add.matrix = [
                [self.matrix[r][c] + other for c in range(self.columns)]
                for r in range(self.rows)]
            return add
        else:
            assert self.same_dimensions_check(other)
            add = Matrix(self.rows, self.columns)
            if not any(isinstance(l, list) for l in self.matrix):
                self.matrix = [self.matrix]
            add.matrix = [
                [self.matrix[r][c] + other.matrix[r][c]
                    for c in range(self.columns)]
                for r in range(self.rows)]
            return add

    def __radd__(self, other):
        """Reverse add function, adds support for format: 2 + bar
           where bar is a Matrix object"""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtraction for matrices
           Accepted formats:
              foo = Matrix(2, 2)
              bar = Matrix(2, 2, 5)
              baz = Matrix(2, 2, 4)
              foo - bar <-> returns a matrix of the form Matrix(2, 2, -5)
              bar - baz <-> returns a matrix of the form Matrix(2, 2, 1)
              bar - 2 <-> returns a matrix of the form Matrix(2, 2, 3)
        """
        return self.__add__(other * -1)

    def transpose(self):
        """Returns the transpose of the matrix"""
        new = Matrix(self.columns, self.rows)
        if not any(isinstance(l, list) for l in self.matrix):
            self.matrix = [self.matrix]
        new.matrix = [[row[i] for row in self.matrix]
                      for i in range(self.columns)]
        return new

    def __mul__(self, other):
        """Matrix multiplication, supports scalar multiplication and
           regular matrix multiplication. First checks dimensions to
           see if multiplication is possible for regular matrix multiplication.
           Accepted formats:
              foo = Matrix(2, 2)
              bar = Matrix(2, 2, 5)
              print foo * bar <-> returns a matrix of the form Matrix(2,2,0)
              print bar * 2 <-> returns a matrix of the form Matrix(2,2,10)
        """
        if isinstance(other, (int, long, float)):
            new = Matrix(self.rows, self.columns)
            if not any(isinstance(l, list) for l in self.matrix):
                self.matrix = [self.matrix]
            new.matrix = [[self.matrix[r][c] * other
                          for c in range(self.columns)]
                          for r in range(self.rows)]
            return new
        else:
            assert self.multiply_check(other)
            new = Matrix(self.rows, other.columns)
            temp_other = other.transpose()
            if not any(isinstance(l, list) for l in self.matrix):
                self.matrix = [self.matrix]
            for x in range(self.rows):
                for y in range(temp_other.rows):
                    new.matrix[x][y] = dot_product(self.matrix[x],
                                                   temp_other.matrix[y])
            return new

    def __rmul__(self, other):
        """Reverse multipy function, adds support for format: 2 * bar
           where bar is a Matrix object"""
        return self.__mul__(other)

    def multiply_expanded(self, other):
        """Matrix multiplication that shows expanded dot product.
           First checks dimensions to see if multiplication is possible for
           regular matrix multiplication.
           Accepted formats:
              foo = Matrix(2, 2)
              bar = Matrix(2, 2, 5)
              print foo * bar <-> returns a matrix of the form Matrix(2,2,0)
        """
        assert self.multiply_check(other)
        new = Matrix(self.rows, other.columns)
        temp_other = other.transpose()
        if not any(isinstance(l, list) for l in self.matrix):
            self.matrix = [self.matrix]
        for x in range(self.rows):
            for y in range(temp_other.rows):
                new.matrix[x][y] = expanded_dot_product(self.matrix[x],
                                                        temp_other.matrix[y])
        return new

    def change_element(self, row, column, new_element):
        """Changes the element in the specified row and the specified column to
           new_element. """
        assert row > 0 and column > 0
        self.matrix[row - 1][column - 1] = new_element

    def symmetric_check(self):
        """Checks if a matrix is symmetric.
           eg: transpose(A) = A
        """
        return self == self.transpose()

    def skew_symmetric_check(self):
        """Checks if a matrix is skew symmetric (anti-symmetric).
           eg: transpose(A) = -A"""
        return -1 * self == self.transpose()

    def augment(self, other):
        """Augments other to self. First checks if number of rows are equal
           eg: if self = 1 2   and   other = 5
                         3 4                 5

               self.augment(other)  returns   1 2 5
                                              3 4 5
        """
        assert self.rows == other.rows
        aug = Matrix(self.rows, self.columns + other.columns)
        for row in range(self.rows):
            for col1 in range(self.columns):
                aug.matrix[row][col1] = self.matrix[row][col1]
            for col2 in range(other.columns):
                aug.matrix[row][col2 + self.columns] = other.matrix[row][col2]
        return aug

    def linear_equation_print(self):
        """Prints the matrix as a system of linear equations. Assumes that an
           augmented matrix is given and so the last column is the system
           constants while the rest of the matrix are the system
           coefficients."""
        temp = []
        for row in self.matrix:
            eq = str()
            for var in range(len(row[:-1])):
                row_str = str("(" + str(row[var]) + ")" +
                              "x" + str(var + 1) + " + ")
                eq += row_str.rjust(space_length(self.matrix) + 7)
            temp.append(eq[:-3] + " = " + str(row[-1]))
        return '\n'.join(temp) + "\n"

    def vector_equation_print(self):
        """Prints the matrix as a system of linear equations. Assumes that an
        augmented matrix is given and so the last column is the system
        constants while the rest of the matrix are the system coefficients."""
        coefficients = Matrix(self.transpose().matrix[:-1]).transpose()
        constants = Matrix(self.transpose().matrix[-1]).transpose()
        equals = Matrix(self.rows, 1, " ")
        equals.change_element(self.rows / 2, 1, "=")
        variables = Matrix(["x" + str(i + 1)
                            for i in range(self.rows)]).transpose()
        return coefficients.augment(
            Matrix(self.rows, 1, " ")
        ).augment(variables).augment(equals).augment(constants)

    def P(self, row_i, row_j):
        """Permutes the row_i'th and row_j'th rows in self.matrix in place"""
        assert row_i > 0 and row_j > 0
        temp = self.matrix[row_i - 1]
        self.matrix[row_i - 1] = self.matrix[row_j - 1]
        self.matrix[row_j - 1] = temp

    def M(self, row, scalar):
        """Multiply every element of the row'th row by nonzero scalar"""
        assert row > 0 and scalar != 0
        self.matrix[row - 1] = [scalar * element
                                for element in self.matrix[row - 1]]

    def A(self, row_i, row_j, scalar):
        """Adds to the elements of the row_j'th row the scalar * the
           corresponding elements of the row_i'th row."""
        assert row_i > 0 and row_j > 0
        self.matrix[row_j - 1] = [a + scalar * b for a, b in zip(
            self.matrix[row_j - 1], self.matrix[row_i - 1])]

    def row_echelon_check(self):
        """Checks if a matrix is in row echelon form"""
        assert self.valid_check()
        if self == Matrix(self.rows, self.columns):
            return True
        if not all(first_nonzero(row) == 1 or
                   first_nonzero(row) == 0 for row in self.matrix):
            return False
        positions = [one_position(self.matrix[rowNum], rowNum)
                     for rowNum in range(self.rows)]
        return all(after > before for before, after in zip(
            positions, positions[1:]))
