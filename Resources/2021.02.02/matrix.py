from typing import Union


class InvalidMatrixError(TypeError):

    def __init__(self, message: str, reason: str):
        super().__init__(message)
        self.reason = reason


class NotSquareMatrixError(TypeError):
    pass


class Matrix:

    def __init__(self, data: Union[list, tuple]):
        if not isinstance(data, (list, tuple)):
            raise TypeError(f'list or tuple expected {type(data)} found')

        if data:
            if not isinstance(data[0], (list, tuple)):
                raise TypeError(f'list or tuple expected {type(data[0])} found')

            columns = len(data[0])
            for row in data[1:]:
                if not isinstance(row, (list, tuple)):
                    raise TypeError(f'list or tuple expected {type(row)} found')

                if len(row) != columns:
                    raise InvalidMatrixError('inconsistant matrix structure', 'dimension')

        self._data = data

    def __repr__(self) -> str:
        return f'Matrix({self._data})'

    @staticmethod
    def from_zeros(rownum: int, colnum: int):
        return Matrix([[0, 0], [0, 0]])

    def transpose(self):
        self._data = list(zip(*self._data))


class SquareMatrix(Matrix):

    def __init__(self, data: Union[list, tuple]):
        super().__init__(data)

        if data:
            rownum = len(data)
            if rownum != len(data[0]):
                raise NotSquareMatrixError('Row and column number missmatch')

    def determinant(self):
        pass

    def inverse(self):
        pass


class MatrixSerializer:

    def save_to_file(self, filepath: str):
        with open(filepath, 'w') as fd:
            for row in self._data:
                fd.write(','.join(map(str, row)))
                fd.write('\n')

    def read_from_file(self, filepath: str):
        with open(filepath, 'r') as fd:
            self._data = []
            for line in fd:
                self._data.append(list(map(int, line.split(','))))


class PersistantSquareMatrix(SquareMatrix, MatrixSerializer):

    def __init__(self, data: Union[list, tuple]):
        super().__init__(data)


if __name__ == '__main__':
    print(Matrix([]))
    try:
        m = Matrix([[1, 2], [3, 4]])
        m.transpose()
        print(m)
    except InvalidMatrixError as invex:
        print(invex.reason)

    sqm = SquareMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sqm.transpose()
    print(sqm)

    persistant_matrix = PersistantSquareMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    persistant_matrix.transpose()
    persistant_matrix.save_to_file('matrix.txt')

    new_matrix = PersistantSquareMatrix([])
    new_matrix.read_from_file('matrix.txt')
    print(new_matrix)
