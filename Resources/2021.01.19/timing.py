import math
import random
from functools import wraps
from datetime import datetime
from time import perf_counter, sleep


def timing(log_file_path: str, threashhold: float) -> callable:
    def perfomance_meter(func: callable) -> callable:
        @wraps(func)
        def time_wrapper(*args: tuple, **kwargs: dict):
            start = perf_counter()
            result = func(*args, **kwargs)
            elapsed = perf_counter() - start

            if elapsed < threashhold:
                return result

            with open(log_file_path, 'a') as fd:
                fd.write(
                    ''.join((
                        datetime.now().isoformat(),
                        ' - ',
                        func.__name__,
                        '(',
                        ', '.join(map(str, args)),
                        ', '.join((f'{k} = {v}' for k, v in kwargs.items())),
                        ')',
                        ' execution time: ',
                        str(elapsed),
                        '\n'
                    ))
                )
            return result
        return time_wrapper
    return perfomance_meter


@timing('timing.log', 2.0)
def factorial(n: int) -> int:
    sleep(random.randint(1, 5))
    return math.factorial(n)


# @timing
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(factorial(20))
    print(factorial(5))
    print(factorial(10))
    print(factorial(n=12))
    # print(fibonacci(32))
