from copy import deepcopy


class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x   # attribute
        self.y = y

        # self.coords = (x, y)
        # self.coords = {'x': x, 'y': y}

    def to_tuple(self):   # method
        return (self.x, self.y)


class Line:

    COUNT: int = 0  # static attribute
    NAME: str = 'Line Object'

    def __init__(self, start: Point, end: Point):
        if not isinstance(start, Point):
            raise TypeError(f'Instance of Point expected {type(start)} found')

        if not isinstance(end, Point):
            raise TypeError(f'Instance of Point expected {type(end)} found')

        self.__a = start
        self.__b = end

        Line.COUNT += 1

    def __del__(self):
        Line.COUNT -= 1

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'Instance of Point expected {type(value)} found')
        self.__a = value

    @a.deleter
    def a(self):
        self.__a = Point(0, 0)

    def __get_b(self):
        return self.__b

    def __set_b(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'Instance of Point expected {type(value)} found')
        self.__b = value

    def __del_b(self):
        self.__b = Point(0, 0)

    b = property(__get_b, __set_b, __del_b)

    def to_tuple(self):
        return (self.__a.to_tuple(), self.__b.to_tuple())

    @staticmethod
    def copy_from(obj: object) -> object:
        return Line(Point(obj.__a.x, obj.__a.y), Point(obj.__b.x, obj.__b.y))

    @staticmethod
    def get_cls_name() -> str:
        return Line.NAME


if __name__ == '__main__':
    a = Point(10, 20)
    b = Point(15, 25)
    line = Line(a, b)
    print('>>> Property', line.a)
    line.a = Point(100, 100)
    print(line.a.to_tuple())
    del line.a
    print(line.a.to_tuple())

    print(line.b.to_tuple())

    print(Line.COUNT)
    second_line = Line(Point(), Point(1, 1))
    print(Line.COUNT)

    copied_line = Line.copy_from(second_line)

    print(second_line.to_tuple())
    print(copied_line.to_tuple())
    print(Line.COUNT)
    print(line.get_cls_name())
    
