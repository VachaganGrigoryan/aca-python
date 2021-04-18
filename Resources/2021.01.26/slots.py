class Point:

    __slots__ = 'x', 'y'

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self):
        pass


class Record:
    pass


def to_dict(self):
    return {'x': self.x, 'y': self.y}


if __name__ == '__main__':
    a = Point(1, 2)
    a.convert_dict = to_dict
    # print(a.convert_dict())

    print(to_dict(a))

    '''b = Point(0, 0)
    print(b.to_dict())

    person = Record()
    person.first_name = 'John'
    print(person.first_name)'''
