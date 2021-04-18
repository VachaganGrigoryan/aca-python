import random
from functools import wraps

from urllib.request import urlopen


def retry(count: int) -> callable:
    def retrier(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            err = None
            local_count = count

            while local_count > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    local_count -= 1
                    err = exc
                    print('Retring function', func.__name__, 'for', local_count, 'times')

            raise err
        return wrapper
    return retrier


@retry(5)
def download_page(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode()[:30]


@retry(5)
def generate_even():
    number = random.randint(1, 200)
    if number % 2 != 0:
        raise ValueError('Not an even number')
    return number


if __name__ == '__main__':
    print(download_page('https://google.com'))
    print(download_page('https://python.org'))
    print(generate_even())
    print(generate_even())
