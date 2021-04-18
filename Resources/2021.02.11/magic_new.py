from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __eq__(self, other) -> bool:
        return NotImplemented


class Rectangle(Shape):

    def __init__(self, height: int, width: int):
        super().__init__()
        self.height = height
        self.width = width

    def __repr__(self) -> str:
        return f'Rectangle({self.height}, {self.width})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Rectangle)\
               and self.height == other.height and self.width == other.width


class Triangle(Shape):

    def __init__(self, a: int, b: int, c: int):
        super().__init__()

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid triangle edges')

        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Triangle)\
               and self.a == other.a and self.b == other.b and self.c == other.c

    def __ne__(self, other) -> bool:
        return not isinstance(other, Triangle)\
               or self.a != other.a or self.b != other.b or self.c != other.c


class Shapes(list):

    def append(self, value):
        if not isinstance(value, Shape):
            raise TypeError('Shapes can only contain shape objects')
        super().append(value)

    def __contains__(self, value) -> bool:
        if not isinstance(value, Shape):
            raise TypeError('Can only lookup shape in Shapes')
        return super().__contains__(value)


if __name__ == '__main__':
    list_of_shapes = Shapes()
    list_of_shapes.append(Rectangle(10, 20))
    list_of_shapes.append(Rectangle(5, 10))
    list_of_shapes.append(Triangle(12, 12, 12))
    list_of_shapes.append(Rectangle(7, 7))
    list_of_shapes.append(Triangle(5, 5, 5))

    print(list_of_shapes)
    print(Rectangle(5, 10) != Rectangle(8, 12))

    print(Rectangle(8, 12) in list_of_shapes)
    print(Rectangle(5, 10) in list_of_shapes)
    print(14 in list_of_shapes)

    # r1 + r2  -> r1.__add__(r2)
    # r2 + r1  -> r2.__add__(r1)
    # o2 + r1  -> r1.__radd__(o2)
    # r1 += r2 -> r1.__iadd__(r2)
