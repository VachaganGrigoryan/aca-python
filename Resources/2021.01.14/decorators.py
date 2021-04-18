from functools import wraps
from datetime import datetime


def hello(func: callable) -> callable:
    @wraps(func)
    def inner():
        print('Hello')
        func()
    return inner


def custom_message(msg: str) -> callable:
    def message_wrapper(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            print(msg)
            return func(*args, **kwargs)  # decorated function
        return wrapper
    return message_wrapper


@hello  # name = hello(name)
def name():
    print('Alice')


@hello  # male_name = hello(male_name)
def male_name():
    print('Bob')


"""
custom_message('Hello world')
|
+--> message_wrapper
     |
     +--- @message_wrapper
          def number_of_day():
              ...
"""
@custom_message('Say something')  # custom_message('Hello world') -> decorator
def number_of_day():
    print(14)


@custom_message('Adding numbers')
def add_numbers(a: int, b: int) -> int:
    return a + b


@custom_message('Summing up the numbers')
def xsum(arr: list) -> int:
    return sum(arr)


if __name__ == '__main__':
    name()
    male_name()
    number_of_day()
    print(add_numbers(14, 0))
    print(add_numbers(10, b=4))
    print(xsum(range(100)))
