#!/usr/bin/env python
"""Brain Prime Functions."""


from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 21


def make_correct_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    print('Question: {0}'.format(number))
    if number == 1:
        return 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'
