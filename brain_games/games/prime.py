#!/usr/bin/env python
"""Brain Prime Functions."""


from random import randrange


def make_correct_answer():
    start, end = 1, 20
    number = randrange(start, end)
    print('Question: {0}'.format(number))
    if number == 1:
        return 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'
