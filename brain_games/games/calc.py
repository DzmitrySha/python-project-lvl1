#!/usr/bin/env python
"""Brain-Calc Functions."""


from random import randint, choice
from operator import add, sub, mul


TASK = 'What is the result of the expression?'


def make_correct_answer():
    start, end = 1, 12
    num1 = randint(start, end)
    num2 = randint(start, end)
    operator, op_symbol = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    print('Question: {0} {1} {2}'.format(num1, op_symbol, num2))
    correct_answer = operator(num1, num2)
    return str(correct_answer)
