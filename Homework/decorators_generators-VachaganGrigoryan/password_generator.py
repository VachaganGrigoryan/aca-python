"""
    Create password generator, the passwords must have
    At least 8 characters.
    Both uppercase and lowercase letters.
    Contains letters and numbers.
    Contains at least one special character, e.g., ! @ # ? ] , do not contains < or > in password
    Generator must have argument for password length. Use itertools functions for this generator.
"""

import itertools
from string import ascii_letters, punctuation, digits


def generate_password(length=8):
    symbol_list = f'{ascii_letters}{punctuation}{digits}'
    for item in itertools.product(symbol_list, repeat=length):
        # if any(map(str.isupper, item)) \
        #         and any(map(str.islower, item)) \
        #         and any(map(str.isdigit, item)) \
        #         and any(c in punctuation for c in item):
        if any(map(lambda elm:
                   elm.isupper()
                   and elm.islower()
                   and elm.isdigit()
                   and elm in punctuation, item)):
            yield ''.join(item)


if __name__ == '__main__':

    with open('pass.txt', 'w+') as pwd_file:

        for pwd in generate_password(8):
            print(pwd)
            pwd_file.write(f'{pwd}\n')
