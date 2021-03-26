def levenshtein(a, b):

    lev = [
        [
            i + j if i == 0 or j == 0 else None for j in range(len(b) + 1)
        ] for i in range(len(a) + 1)
    ]

    for i in range(1, len(lev)):
        for j in range(1, len(lev[i])):
            if a[i - 1] == b[j - 1]:
                lev[i][j] = lev[i - 1][j - 1]
            else:
                lev[i][j] = min(lev[i - 1][j], lev[i][j - 1], lev[i - 1][j - 1]) + 1

    return lev[-1][-1]


def soundex(text):
    text = text.upper()
    encoding_table = {
        '': 'AEHIOUWY',
        '1': 'BFPV',
        '2': 'CGJKQSXZ',
        '3': 'DT',
        '4': 'L',
        '5': 'MN',
        '6': 'R'
    }
    soundex_number = text[0]
    for symboly in text[1:]:
        for number in encoding_table:
            if symboly in encoding_table[number]:

                soundex_number = f'{soundex_number}{number}'

    return f'{soundex_number[:4]:0<4s}'


if __name__ == '__main__':

    print(soundex("Robert"))
    print(soundex("Rupert"))
    print(soundex('Rubin'))
    print(soundex('Ashcraft'))
    print(soundex('Ashcroft'))
    print(soundex('Tymczak'))
    print(soundex('Honeyman'))