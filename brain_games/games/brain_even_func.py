#!/usr/bin/env python
"""Brain-Even Functions."""


from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_correct_answer():
    start, end = 1, 99
    number = randint(start, end)
    print('Question: {0}'.format(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
