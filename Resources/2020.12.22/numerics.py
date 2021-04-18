import sys


print('char  |  isnumeric  |  isdigit  |  isdecimal  ')
for code in range(sys.maxunicode + 1):
    char = chr(code)
    numeric, digit, decimal = char.isnumeric(), char.isdigit(), char.isdecimal()
    if numeric or digit or decimal:
        print('------+-------------+-----------+--------------')
        print(
            f'{char:<6}',
            '{:<12}'.format(str(numeric)),
            f'{str(digit):<10}',
            '{:<12}'.format(str(decimal)),
            sep='| '
        )
