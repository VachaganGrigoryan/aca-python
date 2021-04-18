from collections.abc import Iterator


class Countdown:

    def __init__(self, top: int):
        if top <= 0:
            raise ValueError('Countdown top must be a positive integer')
        self.__top = top

    def __iter__(self):
        return self

    def __next__(self):
        if self.__top < 0:
            raise StopIteration()
        value = self.__top
        self.__top -= 1
        return value


class CountdownWithMixin(Iterator):

    def __init__(self, top: int):
        if top <= 0:
            raise ValueError('Countdown top must be a positive integer')
        self.__top = top

    def __next__(self):
        if self.__top < 0:
            raise StopIteration()
        value = self.__top
        self.__top -= 1
        return value


class IterableFile(Iterator):

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.fd = open(filepath, 'r')

    def __del__(self):
        print('>>> Closing file')
        self.fd.close()

    def __next__(self):
        # if line := self.fd.readline():

        line = self.fd.readline().strip()
        if line:
            return line
        raise StopIteration()


if __name__ == '__main__':
    cdown = Countdown(3)

    print(next(cdown))
    print(next(cdown), end='\n\n')

    for num in Countdown(10):  # iter(Countdown(10)) -> .__next__
        print(num)

    for line in IterableFile('datafile.txt'):
        print(line)

    print('Everything is over')

