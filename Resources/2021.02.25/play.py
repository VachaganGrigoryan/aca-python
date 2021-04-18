from sys import getsizeof
from typing import NamedTuple
from collections import (
    OrderedDict,
    defaultdict,
    namedtuple,
)


class Person(namedtuple('ImmutablePerson', ('first_name', 'last_name'))):

    __slots__ = ()

    def say_hello(self) -> str:
        return f'Hello {self.first_name} {self.last_name}'


def ordered_dict():
    data = {
        'first_name': 'John',
        'age': 30
    }

    ordered_data = OrderedDict([
        ('first_name', 'John'),
        ('age', 30)
    ])

    print(data)
    print(ordered_data['age'])


def default_dict():
    data = {}
    def_dict = defaultdict(list)

    if 'a' in data:
        data['a'].append(1)
    else:
        data['a'] = [1]

    # data['a'] = data.get('a', 0) + 1
    # data.get('a', []).append(1)
    data['a'] = data.get('a', []) + [1]

    def_dict['a'].append(1)  # list_factory() -> []

    print(data)
    print(def_dict)

    tree_data = tree()
    tree_data['first']['second']['third'] = 'We have done it'
    print(tree_data)


def tree():
    return defaultdict(tree)


def named_tuple():
    person_dict = {
        'first_name': 'John',
        'last_name': 'Dow',
        'age': 30
    }

    person_tuple = ('John', 'Dow', 30)

    person = namedtuple('Person', ('first_name', 'last_name', 'age'))
    print('On the fly created class:', person)
    person_data = person('John', 'Dow', age=30)
    second_person = person('Jane', 'Dow', age=28)

    print(person_data)
    print(second_person)
    print(isinstance(second_person, tuple))
    print(person_data.age)
    print(person_data[0])
    # person_data.age = 35

    print('Dict size:', getsizeof(person_dict))
    print('NamedTuple size:', getsizeof(person_data))

    print(person_dict['first_name'])
    print(person_data.first_name)
    print(person_data._replace(last_name='Smith'))
    print(person_data._asdict())

    print('Converting dictionary to named tuple')
    print(dict_to_named_tuple(
        {'country': 'AM', 'capital': 'Yerevan', 'phonecode': '+374'},
        'CountryData'
    ))


def dict_to_named_tuple(data: dict, typename: str = 'VO') -> NamedTuple:
    return namedtuple(typename, data.keys())(**data)


def class_test():
    p = Person('Mike', 'Smith')
    print(p)
    print(p.say_hello())
    # p.age = 40
    # print(p.age)
    # p.first_name = 'John'
    

if __name__ == '__main__':
    print(Person)
    named_tuple()

