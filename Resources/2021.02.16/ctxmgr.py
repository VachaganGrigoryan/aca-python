from contextlib import AbstractContextManager, contextmanager


class XOpen(AbstractContextManager):

    def __init__(self, filepath: str, mode: str = 'r'):
        super().__init__()

        self.filepath = filepath
        self.mode = mode
        self.descriptor = None

    def __enter__(self):
        print('>>> entering the context')
        self.descriptor = open(self.filepath, self.mode)
        return self.descriptor

    def __exit__(self, exc_type, exc_value, traceback):
        print('>>> exitting the context')
        if exc_type:
            print('exc_type =', exc_type)
            print('exc_value =', exc_value)
            print('traceback =', traceback)

        self.descriptor.close()
        self.descriptor = None


@contextmanager
def xxopen(filepath: str, mode: str = 'r'):
    try:
        fd = open(filepath, mode)
        yield fd
    finally:
        print('>>> exitting xxopen context')
        fd.close()


if __name__ == '__main__':
    with XOpen('data.txt', 'r') as fd:
        print(fd.readline())
        # raise TypeError('Manually raised exception')
        print(fd.readline())

    print('>>> testing xxopen')
    with xxopen('data.txt', 'r') as fd:
        print(fd.readline())
        raise TypeError('Manually raised exception')
        print(fd.readline())

    fd.seek(0)
