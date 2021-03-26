from typing import Union
from random import random


class InvalidMatrixError(TypeError):

    def __init__(self, message: str, reason: str):
        super().__init__(message)
        self.reason = reason


class Matrix:

    def __init__(self, two_d_array: Union[list, tuple]):
        if not isinstance(two_d_array, (list, tuple)):
            raise TypeError(f'list or tuple expected {type(two_d_array)} found')

        if two_d_array:
            for row in two_d_array:
                if not isinstance(row, (list, tuple)):
                    raise TypeError(f'list or tuple expected {type(row)} found')

                if len(row) != len(two_d_array[0]):
                    raise InvalidMatrixError('inconsistent matrix structure', 'dimension')

                if not all(isinstance(elem, (int, float)) for elem in row):
                    raise TypeError(f"unsupported value type. Only the numerical elements are expected.")

        self.data = two_d_array

    def __iter__(self):
        yield from self.data  # return ((elem for elem in row) for row in self.data)

    def __neg__(self):
        return Matrix([[-one for one in row] for row in self.data])

    def __add__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise TypeError(
                f"unsupported operand type({other_matrix}) for +: <class 'Matrix'> and {type(other_matrix)}")

        if not self.same_dimension_with(other_matrix):
            raise InvalidMatrixError("the two matrices must be the same size: The rows and columns must match in size.",
                                     'dimension')

        return Matrix([
            [one + two for one, two in zip(row_one, row_two)] for row_one, row_two in zip(self.data, other_matrix.data)
        ])

    def __sub__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise TypeError(
                f"unsupported operand type({other_matrix}) for -: <class 'Matrix'> and {type(other_matrix)}")

        if not self.same_dimension_with(other_matrix):
            raise InvalidMatrixError("the two matrices must be the same size: The rows and columns must match in size.",
                                     'dimension')

        return Matrix([
            [one - two for one, two in zip(row_one, row_two)] for row_one, row_two in zip(self.data, other_matrix.data)
        ])

    def __mul__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise TypeError(
                f"unsupported operand type({other_matrix}) for *: <class 'Matrix'> and {type(other_matrix)}")

        if len(self.data[0]) != len(other_matrix.data):
            raise InvalidMatrixError("the matrix length is different. [m*n] X [n*p] n's should be same", 'dimension')

        mtx_one = self.data
        mtx_two_t = other_matrix.transposing()
        return Matrix([
            [sum(elem_1 * elem_2 for elem_1, elem_2 in zip(line_1, line_2)) for line_2 in mtx_two_t]
            for line_1 in mtx_one
        ])

    def __str__(self):
        max_len = len(max([max(map(str, row), key=len) for row in self.data], key=len))
        lines = [" ".join(map(lambda elm: str(elm).rjust(max_len), row)) for row in self.data]

        return f'|{lines[0]}|' if len(lines) < 2 else '\n'.join([
            f'⌈ {lines[0]} ⌉',
            *(f'| {item} |' for item in lines[1:-1]),
            f'⌊ {lines[-1]} ⌋'
        ])

    def transposing(self):
        return Matrix(list(zip(*self.data)))

    def determinant(self):
        if not self.is_square():
            raise InvalidMatrixError("<class 'Matrix'> must be a square matrix: Can't calculate Determinant",
                                     'dimension')

        data = self.data
        if len(data) == 2:
            return data[0][0] * data[1][1] - data[0][1] * data[1][0]

        det_2x2s = [((-1) ** i) * elem * Matrix([
            line[:i] + line[i + 1:] for line in data[1:]
        ]).determinant() for i, elem in enumerate(data[0])]

        return sum(det_2x2s)

    def inverse(self):
        det = self.determinant()

        if det == 0:
            raise InvalidMatrixError('determinant cannot be zero: the matrix have not the inverse matrix', 'singular')

        adj_matrix = self.adjugate_matrix()
        return Matrix([
            [(1 / det) * elem for elem in row]
            for row in adj_matrix
        ])

    def adjugate_matrix(self):
        data = self.data
        return Matrix([[(-1) ** (i + j) * Matrix([
            line[:j] + line[j + 1:] for line in data[:i] + data[i + 1:]
        ]).determinant() for i in range(len(data))] for j in range(len(data))])

    def same_dimension_with(self, other_matrix):
        return len(self.data) == len(other_matrix.data) and \
               len(self.data[0]) == len(other_matrix.data[0])

    def is_square(self):
        return len(self.data) == len(self.data[0])

    @staticmethod
    def random_matrix(n, m):
        return Matrix([[random() for __ in range(m)] for _ in range(n)])


if __name__ == '__main__':
    matrix = Matrix([
        [1.60, 3.1, 42.34],
        [4.0, 5.00, 6.9],
        [43.0, 2.4, 3.99],
    ])
    print(matrix)
    # print(matrix.determinant())
    # print(matrix.inverse())
    # Determinant
    matrix = Matrix([
        [1, 0, 4, -6],
        [2, 5, 0, 3],
        [-1, 2, 3, 5],
        [2, 1, -2, 3],
    ])
    print(matrix)
    print(matrix.determinant())

    # Random
    # print(Matrix.random_matrix(1, 6))
    # print(Matrix.random_matrix(2, 2))
    print(Matrix.random_matrix(3, 3))

    # Inverse
    matrix = Matrix([
        [1, 1, 1, -1],
        [1, 1, -1, 1],
        [1, -1, 1, 1],
        [-1, 1, 1, 1],
    ])
    print(matrix)
    print(matrix.inverse())

    # The Matrix.__mul__() function
    mtx_1 = Matrix([
        [1, 2, 3]
    ])

    mtx_2 = Matrix([
        [4],
        [5],
        [6]
    ])

    mtx_3 = mtx_1 * mtx_2

    print(mtx_1)
    print(mtx_2)
    print(mtx_3)
    #
    mtx_1 = Matrix([
        [1, 2, 3]
    ])

    mtx_2 = Matrix([
        [4],
        [5],
        [6]
    ])

    mtx_3 = mtx_2 * mtx_1

    print(mtx_2)
    print(mtx_1)
    print(mtx_3)
    #
    mtx_1 = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])

    mtx_2 = Matrix([
        [7, 8],
        [9, 10],
        [11, 12]
    ])

    mtx_3 = mtx_1 * mtx_2

    print(mtx_1)
    print(mtx_2)
    print(mtx_3)

    # The Matrix.__add__() and Matrix.__sub__()
    # mtx_1 = Matrix([
    #     [3, 8],
    #     [4, 6]
    # ])
    # mtx_2 = Matrix([
    #     [4, 0],
    #     [1, -9]
    # ])
    # print(mtx_1 + mtx_2)
    # print(mtx_1 - mtx_2)
    # print(-mtx_2)
