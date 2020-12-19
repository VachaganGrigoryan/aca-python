"""
    Գրել ռեկուրսիվ ֆունկցիա, որը կվերադարձնի զանգվածի ամենափոքր էլեմենտը:
"""


def min_elem(array, melm=None):

    if not array:
        return melm

    if melm is None:
        melm = array[-1]

    elem = array.pop()
    if melm > elem:
        melm = elem

    return min_elem(array, melm)


# print(min_elem([]))


def find_min(array):

    if len(array) < 2:
        return array.pop()

    min_elem = array.pop()

    if min_elem < array[-1]:
        array[-1] = min_elem

    return find_min(array)


# print(min_elem([12, 54, 96, 5, 62, 8, -1]))



















































