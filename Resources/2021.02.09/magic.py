from typing import Union


class FullControll:

    def __new__(cls, *args, **kwargs):
        # business logic
        return super(FullControll, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass


class Matrix:

    def __init__(self, m: Union[list, tuple]):
        super().__init__()

        # TODO: implement matrix validation
        self.data = m
        self.rownum = len(self.data)
        self.colnum = len(self.data[0])

    def __repr__(self) -> str:
        return f'Matrix({self.data})'

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Can only add Matrix to another Matrix')

        self_data = self.data
        other_data = other.data
        columns = len(self_data[0])

        result = [
            [
                self_data[rowid][colid] + other_data[rowid][colid]
                for colid in range(columns)
            ] for rowid in range(len(self_data))
        ]

        return Matrix(result)

    def __getitem__(self, key: Union[int, tuple]):
        # TODO: add more validations
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, tuple):
            return self.data[key[0]][key[1]]

    def __setitem__(self, key: Union[int, tuple], value):
        if isinstance(key, int):
            if not isinstance(value, list):
                raise TypeError('Value must be of list')

            if len(value) != self.colnum:
                raise TypeError()

            self.data[key] = value
        elif isinstance(key, tuple):
            if not isinstance(value, (int, float)):
                raise TypeError('Value must be of list')
            self.data[key[0]][key[1]] = value

    def __call__(self):
        return Matrix(self.data)

    def __str__(self) -> str:
        return str(self.data).replace('[', '').replace(']', '')


class WebAPI:

    def __init__(self, host: str):
        self.host = host

    def web_call(self, url: str, *args, **kwargs):
        return args, kwargs

    def __getattr__(self, name: str):
        url = f'{self.host}/{name.replace("_", "-")}'
        return lambda *args, **kwargs: self.web_call(url, *args, **kwargs)

    def get_all_users(self):
        pass


class Function:

    def __new__(cls, *args, **kwargs):
        inst = super(Function, cls).__new__(cls)
        return inst(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('This is function body')
        return args, kwargs


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    m3 = m1 + m2  # type(m1).__add__(m1, m2)
    print(m3[1, 0])
    print(m3[1])

    m3[1] = [-1, -2]
    m3[1, 1] = 100
    print(repr(m3))

    m4 = m3()
    print(str(m4))

    client = WebAPI('https://api.com')
    print(client.get_user(name='John'))
    print(client.get_client(name='John'))
    client.get_all_users()

    print(Function(True, 14, name='John'))
