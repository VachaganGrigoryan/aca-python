import math
from abc import ABC, abstractmethod


class Shape2D(ABC):

    '''@property
    @abstractmetod
    def name(self):
        pass'''

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @classmethod
    def from_file(cls, path: str):
        with open(path, 'r') as fd:
            return cls(*map(float, fd.read().split(',')))


class Rectangle(Shape2D):

    def __init__(self, a: float, b: float, *args: tuple):
        super().__init__()
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f'Rectangle({self.a}, {self.b})'

    def perimeter(self) -> float:
        return 2 * self.a + 2 * self.b

    def area(self) -> float:
        return self.a * self.b

    def draw(self):
        print('>>> Drawing', repr(self))


class Square(Rectangle):

    def __init__(self, side: float, *args: tuple):
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f'Square({self.a})'

    def area(self) -> int:
        return int(super().area())

    def draw(self):
        print('>>> Drawing', repr(self))


class Triangle(Shape2D):

    def __init__(self, a: float, b: float, c: float, *args: tuple):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def draw(self):
        print('>>> Drawing', repr(self))


if __name__ == '__main__':
    shapes = [
        Rectangle(10.3, 20.2),
        Square(15.3),
        Square(17),
        Triangle(10, 10, 10)
    ]

    for shape in shapes:
        print('Area of', repr(shape), 'is', shape.area())

    print(Rectangle.from_file('rect.txt'))
    print(Square.from_file('rect.txt'))
