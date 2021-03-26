import random
from retry import retry
from password_generator import generate_password


@retry((Exception, IndexError), tries=5, delay=1, backoff=2, logger=None)
def random_numbers_interval(p, q):
    """ function generates rundom number in interval [0,1], p, q are from [0,1] interval
     ...

     if random_number<p:
         raise Exception('less than lower bound')
     if random_number>q:
         raise Exception('grader than upper bound')
     ...
    """
    random_number = random.randint(0, 10)
    print(f"{q} < {random_number} < {p}")
    if random_number < p:
        raise Exception('less than lower bound')
    if random_number > q:
        raise Exception('grader than upper bound')

    return p + q


# print(random_numbers_interval(2, 5))

pwd = generate_password(8)

print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))