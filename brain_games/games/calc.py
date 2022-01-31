#!/usr/bin/env python
"""Brain-Calc Functions."""


from random import randint, choice
from operator import add, sub, mul


MIN_NUMBER = 1
MAX_NUMBER = 12


def make_correct_answer():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator, op_symbol = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    print('Question: {0} {1} {2}'.format(num1, op_symbol, num2))
    correct_answer = operator(num1, num2)
    return str(correct_answer)
