from collections.abc import MutableSequence


class MutableString(MutableSequence):

    def __init__(self, value):
        super(MutableString, self).__init__()
        self.str = bytearray(str(value), 'utf-8')

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("<class 'MutableString'> indices must be integers.")
        if abs(index) > len(self.str) - 1:
            raise IndexError("<class 'MutableString'> index out of range.")
        return MutableString(self.str.decode()[index])

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("<class 'MutableString'> indices must be integers.")

        if abs(index) > len(self.str) - 1:
            raise IndexError("<class 'MutableString'> assignment index out of range.")

        if index < 0:
            index = len(self.str) + index

        self.str[index:index + 1] = bytes(str(value), 'utf-8')

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("<class 'MutableString'> indices must be integers.")
        if abs(index) > len(self.str) - 1:
            raise IndexError("<class 'MutableString'> assignment index out of range.")
        self.str = self.str[:index] + self.str[index + 1:]

    def __str__(self):
        return self.str.decode()

    def __repr__(self):
        return f'MutableString("{self.str.decode()}")'

    def __len__(self):
        return len(self.str.decode())

    def __iter__(self):
        yield from self.str.decode()

    def __add__(self, other):
        if not isinstance(other, MutableString):
            raise TypeError(f'can only concatenate MutableString (not "{type(other)}") to MutableString.')
        return MutableString((self.str + other.str).decode())

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError("<class 'MutableString'> indices must be integers.")
        if abs(index) > len(self.str) - 1:
            raise IndexError("<class 'MutableString'> assignment index out of range.")
        if index < 0:
            index = len(self.str) + index
        self.str[index:index] = bytes(str(value), 'utf-8')

    def title(self):
        return MutableString(self.str.decode().title())

    def capitalize(self):
        return MutableString(self.str.decode().capitalize())

    def center(self, width, fill=None):
        return MutableString(self.str.decode().center(width, fill or " "))

    def upper(self):
        return MutableString(self.str.decode().upper())

    def lower(self):
        return MutableString(self.str.decode().lower())

    def startswith(self, prefix, start=None, end=None):
        return self.str.decode().startswith(prefix, start, end)

    def endswith(self, suffix, start=None, end=None):
        return self.str.decode().endswith(suffix, start, end)

    def find(self, sub, start=None, end=None):
        return self.str.decode().find(sub, start, end)

    def rfind(self, sub, start=None, end=None):
        return self.str.decode().rfind(sub, start, end)

    def index(self, sub, start=None, end=None):
        return self.str.decode().index(sub, start, end)

    def rindex(self, sub, start=None, end=None):
        return self.str.decode().rindex(sub, start, end)

    def split(self, symbol):
        return self.str.decode().split(symbol)

    def replace(self, old, new):
        return MutableString(self.str.decode().replace(old, new))

    # def rreplace(self, old, new):  #
    #     pass

    def isdigit(self):
        return self.str.decode().isdigit()

    def isalpha(self):
        return self.str.decode().isalpha()

    def isalnum(self):
        return self.str.decode().isalnum()

    def islower(self):
        return self.str.decode().islower()

    def isupper(self):
        return self.str.decode().isupper()

    def isspace(self):
        return self.str.decode().isspace()

    def istitle(self):
        return self.str.decode().istitle()

    def join(self, array):
        return MutableString(self.str.decode().join(array))

    def format(self, *args, **kwargs):
        return MutableString(self.str.decode().format(*args, **kwargs))

    # def ord(self, c):
    #     pass
    #
    # def chr(self, d):
    #     pass

    def count(self, sub, start=None, end=None):
        return self.str.decode().count(sub, start, end)

    def lstrip(self, c=None):
        return MutableString(self.str.decode().lstrip(c))

    def rstrip(self, c=None):
        return MutableString(self.str.decode().rstrip(c))

    def strip(self, c=None):
        return MutableString(self.str.decode().strip(c))


if __name__ == '__main__':
    string = MutableString("New String")
    print(string)
    print(string[-6])
    del string[-2]
    print(string)
    string[3] = "Replace"

    string1 = string + MutableString("The other String")
    string1.insert(2, ['string', 5])
    print(string1)

    string1[5] = 'REP'

    st = MutableString([4, 4, 5, 5])
    st.insert(6, ' 6,')
    print(sum(eval(str(st))))

    string = MutableString("   tex{}ts{}   ")
    print(string.title())
    print(string.capitalize())
    print(string.center(53, '*'))

    print(string.upper())
    print(string.lower())
    print(string.startswith('*'))
    print(string.endswith('ts'))
    print(string.find("text"))
    print(string.rfind("xts"))
    print(string.index('t'))
    print(string.rindex('t'))
    print(string.split('t'))
    print(string.join(['4', '45', '45']))
    print(string)
    print(string.format(4, 5))
    print(string.count('t'))
    print(string.lstrip())
    print(string.rstrip())
    print(string.strip())
