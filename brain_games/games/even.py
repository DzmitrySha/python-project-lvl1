#!/usr/bin/env python
"""Brain-Even Functions."""


from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 99


def make_correct_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    print('Question: {0}'.format(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
