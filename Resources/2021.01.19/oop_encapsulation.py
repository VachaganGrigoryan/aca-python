class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x   # attribute
        self.y = y

        # self.coords = (x, y)
        # self.coords = {'x': x, 'y': y}

    def to_tuple(self):   # method
        return (self.x, self.y)


class Line:

    def __init__(self, start: Point, end: Point):
        self.a = start
        self.b = end


class Dummy:
    pass


def point_to_tuple(point: Point) -> tuple:
    return (point.x, point.y)


if __name__ == '__main__':
    a = Point(10, 20)  # Point.__init__(a, 10, 20)
    print(a.to_tuple())  # Point.to_tuple(a)
    print(point_to_tuple(a))

    print(a.x)

    b = Point(15, 25)
    print(b.to_tuple())

    c = Point()
    print(c.to_tuple())

    dummy_object = Dummy()
