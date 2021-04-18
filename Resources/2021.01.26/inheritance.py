class Rectangle:

    __slots__ = '__height', '__width', '_name'

    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self._name = 'Rectangle'

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * self.__height + 2 * self.__width

    @property
    def name(self):
        return self._name


class Square(Rectangle):

    __slots__ = '__length'

    def __init__(self, length: int):
        # Rectangle.__init__(self, length, length)
        # super(Square, self).__init__(length, length)
        super().__init__(length, length)

        self.__length = length
        self._name = 'Sqaure'  # name

    def area(self):
        print('Called for Square')
        return self.__length ** 2

    def show(self):
        pass


if __name__ == '__main__':
    objs = (Rectangle(10, 20), Square(10), Square(15), Rectangle(5, 7))
    for obj in objs:
        print(obj.name, obj.area())

    rect = Rectangle(10, 20)
    print(rect.name, rect.area())

    sq = Square(20)
    print(sq.area())
    print(sq.name)
